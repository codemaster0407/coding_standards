"""
main.py — Coding Standards Pipeline (Groq-only, memory-efficient)

Memory strategy:
  * Every piece of scraped/searched/summarised content is written to disk
    immediately after it is produced and then deleted from memory.
  * Large aggregated strings are never held in RAM; they are built by reading
    individual files on demand, one at a time.
  * Directory layout under context/:
      context/crawled/<slug>.txt       — raw crawled page content
      context/tavily/<key>.json        — one Tavily result per file
      context/summaries/<key>.txt      — one summary per file
      context/coding_standards_extracted.json  — final structured draft
"""

import os
import gc
import json
import time
import asyncio
from dotenv import load_dotenv

from helpers.url_regex import extract_https_urls
from helpers.groq_helper import groq_api_call, chunk_string
from helpers.tavily_search import perform_tavily_search
from helpers.json_to_docx import create_docx_from_json
from webcrawler.crawl import main as crawl_single_url
from pydantic_models.models import TechStackData, DocumentContent
from prompts.gemini_prompts import (
    DATA_EXTRACTION_PROMPT,
    SUMMARISE_CONTEXT_PROMPT,
    FINAL_DRAFT_PROMPT,
)

load_dotenv()

# ---------------------------------------------------------------------------
# Directory constants
# ---------------------------------------------------------------------------
CONTEXT_DIR   = "context"
CRAWLED_DIR   = os.path.join(CONTEXT_DIR, "crawled")
TAVILY_DIR    = os.path.join(CONTEXT_DIR, "tavily")
SUMMARY_DIR   = os.path.join(CONTEXT_DIR, "summaries")
EXTRACTED_JSON = os.path.join(CONTEXT_DIR, "coding_standards_extracted.json")
OUTPUT_DOCX   = "Coding_Standards.docx"


def _setup_dirs():
    for d in [CONTEXT_DIR, CRAWLED_DIR, TAVILY_DIR, SUMMARY_DIR]:
        os.makedirs(d, exist_ok=True)


def _slug(text: str, max_len: int = 60) -> str:
    """Turn a string into a safe filename slug."""
    import re
    return re.sub(r"[^a-z0-9]+", "_", text.lower())[:max_len].strip("_")


# ---------------------------------------------------------------------------
# STEP 1 — Extract metadata (tech stack + tavily prompts + links)
# ---------------------------------------------------------------------------

def step_extract_metadata(question_prompt: str):
    print("\n=== STEP 1: Extracting Tech Stack & Tavily Prompts (Groq) ===")

    links = extract_https_urls(question_prompt)
    print(f"   -> Links found: {links}")

    extracted: TechStackData = groq_api_call(
        prompt=DATA_EXTRACTION_PROMPT,
        raw_text=question_prompt,
        pydantic_class=TechStackData,
    )

    print(f"   -> Tech Stack : {extracted.techstack}")
    print(f"   -> {len(extracted.tavily_search_prompts)} Tavily prompts generated")

    # Persist metadata so it can be inspected / reused
    manifest = {
        "techstack": extracted.techstack,
        "tavily_search_prompts": extracted.tavily_search_prompts,
        "links": links,
    }
    with open(os.path.join(CONTEXT_DIR, "metadata.json"), "w") as fh:
        json.dump(manifest, fh, indent=2)

    return extracted, links


# ---------------------------------------------------------------------------
# STEP 2 — Crawl links: write each page to its own file, free RAM immediately
# ---------------------------------------------------------------------------

async def step_crawl_links(links: list) -> list:
    """
    Crawls each URL and writes content to context/crawled/<slug>.txt.
    Returns a list of file paths (manifest), never the content itself.
    """
    print("\n=== STEP 2: Crawling Links (streaming to disk) ===")
    manifest = []

    for url in links:
        slug = _slug(url)
        out_path = os.path.join(CRAWLED_DIR, f"{slug}.txt")
        print(f"   -> Crawling: {url}")
        try:
            content = await crawl_single_url(url)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(content)
            manifest.append({"url": url, "file": out_path})
            print(f"      Saved {len(content):,} chars → {out_path}")
        except Exception as e:
            print(f"   [WARN] Crawl failed for {url}: {e}")
        finally:
            # Drop the string from memory immediately
            try:
                del content
            except NameError:
                pass
            gc.collect()

    # Save manifest (tiny dict, not the content)
    with open(os.path.join(CRAWLED_DIR, "manifest.json"), "w") as fh:
        json.dump(manifest, fh, indent=2)

    return manifest


# ---------------------------------------------------------------------------
# STEP 3 — Tavily search: write each result to its own JSON file
# ---------------------------------------------------------------------------

def step_tavily_search(tavily_prompts: list) -> list:
    """
    Runs one Tavily search per prompt and writes result to
    context/tavily/query_<N>.json.
    Returns a manifest list, never the full result dicts.
    """
    print("\n=== STEP 3: Tavily Searches (streaming to disk) ===")
    manifest = []

    for i, query in enumerate(tavily_prompts):
        key = f"query_{i + 1:02d}"
        out_path = os.path.join(TAVILY_DIR, f"{key}.json")
        print(f"   -> Search {i + 1}/{len(tavily_prompts)}: {query[:70]}...")
        try:
            result = perform_tavily_search(query)
            payload = {"tavily_search_prompt": query, "data": result}
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, indent=2)
            manifest.append({"key": key, "file": out_path, "prompt": query})
            print(f"      Saved → {out_path}")
        except Exception as e:
            print(f"   [WARN] Search {i + 1} failed: {e}")
        finally:
            try:
                del result, payload
            except NameError:
                pass
            gc.collect()
        time.sleep(1)  # polite pause between searches

    # Save manifest
    with open(os.path.join(TAVILY_DIR, "manifest.json"), "w") as fh:
        json.dump(manifest, fh, indent=2)

    return manifest


# ---------------------------------------------------------------------------
# STEP 4 — Summarise: read one file at a time, write summary, free RAM
# ---------------------------------------------------------------------------

def _summarise_text(raw: str, label: str) -> str:
    """Chunk a raw string, summarise each chunk with Groq, concatenate."""
    chunks = chunk_string(raw)
    parts = []
    for j, chunk in enumerate(chunks):
        if len(chunks) > 1:
            print(f"      Chunk {j + 1}/{len(chunks)}...")
        try:
            part = groq_api_call(
                prompt=SUMMARISE_CONTEXT_PROMPT,
                raw_text=chunk,
                pydantic_class=None,
            )
            parts.append(part)
        except Exception as e:
            print(f"      [WARN] Summary chunk failed ({label}): {e}")
            parts.append(chunk[:500])  # fallback snippet
        finally:
            del chunk
            gc.collect()
    return "\n".join(parts)


def step_summarise_per_area(
    crawl_manifest: list,
    tavily_manifest: list,
) -> list:
    """
    Reads each crawled/tavily file one at a time, summarises it with Groq,
    and writes the summary to context/summaries/<key>.txt.
    Returns a summary manifest (list of file paths).
    Never holds more than one source file's content in RAM at once.
    """
    print("\n=== STEP 4: Summarising Per-Area (Groq, streaming) ===")
    summary_manifest = []

    # --- Tavily summaries ---
    for entry in tavily_manifest:
        key = entry["key"]
        out_path = os.path.join(SUMMARY_DIR, f"{key}.txt")
        print(f"   -> Summarising {key}: {entry['prompt'][:60]}...")
        raw = ""
        try:
            with open(entry["file"], "r", encoding="utf-8") as fh:
                data = json.load(fh)
            lines = [f"Search Query: {data.get('tavily_search_prompt', '')}"]
            for r in data.get("data", {}).get("results", []):
                lines.append(f"\nSource: {r.get('url', '')}")
                lines.append(r.get("content", ""))
            raw = "\n".join(lines)
            del data, lines
            gc.collect()

            summary = _summarise_text(raw, key)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(summary)
            summary_manifest.append({
                "key": key,
                "file": out_path,
                "label": entry["prompt"],
            })
            print(f"      Summary saved → {out_path}")
        except Exception as e:
            print(f"   [WARN] Failed summarising {key}: {e}")
        finally:
            del raw
            try:
                del summary
            except NameError:
                pass
            gc.collect()

    # --- Crawled-URL summaries ---
    for entry in crawl_manifest:
        url = entry["url"]
        key = f"crawled_{_slug(url)}"
        out_path = os.path.join(SUMMARY_DIR, f"{key}.txt")
        print(f"   -> Summarising crawled: {url[:60]}")
        raw = ""
        try:
            with open(entry["file"], "r", encoding="utf-8") as fh:
                raw = fh.read()
            summary = _summarise_text(raw, key)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(summary)
            summary_manifest.append({"key": key, "file": out_path, "label": url})
            print(f"      Summary saved → {out_path}")
        except Exception as e:
            print(f"   [WARN] Failed summarising {url}: {e}")
        finally:
            del raw
            try:
                del summary
            except NameError:
                pass
            gc.collect()

    with open(os.path.join(SUMMARY_DIR, "manifest.json"), "w") as fh:
        json.dump(summary_manifest, fh, indent=2)

    return summary_manifest


# ---------------------------------------------------------------------------
# STEP 5 — Final draft: read summaries one by one, stream sections to disk
# ---------------------------------------------------------------------------

def step_generate_final_draft(summary_manifest: list) -> str:
    """
    Reads each summary file one at a time, sends it to Groq for the final
    structured draft, and appends sections to the output JSON file
    incrementally — so the full document is never in RAM at once.
    """
    print("\n=== STEP 5: Generating Final Draft (Groq, streaming to disk) ===")

    # Open the output JSON file and write the opening bracket
    with open(EXTRACTED_JSON, "w", encoding="utf-8") as out_fh:
        out_fh.write('{"sections": [\n')
        first_section = True

        for entry in summary_manifest:
            label = entry.get("label", entry["key"])
            print(f"   -> Drafting section for: {label[:60]}")
            raw = ""
            try:
                with open(entry["file"], "r", encoding="utf-8") as fh:
                    raw = fh.read()

                chunks = chunk_string(raw)
                for j, chunk in enumerate(chunks):
                    if len(chunks) > 1:
                        print(f"      Chunk {j + 1}/{len(chunks)}...")
                    try:
                        result: DocumentContent = groq_api_call(
                            prompt=FINAL_DRAFT_PROMPT,
                            raw_text=chunk,
                            pydantic_class=DocumentContent,
                        )
                        for section in result.sections:
                            if not first_section:
                                out_fh.write(",\n")
                            out_fh.write(
                                json.dumps(section.model_dump(), ensure_ascii=False)
                            )
                            first_section = False
                        out_fh.flush()
                    except Exception as e:
                        print(f"      [WARN] Draft chunk failed: {e}")
                    finally:
                        del chunk
                        gc.collect()

            except Exception as e:
                print(f"   [WARN] Skipping {entry['key']}: {e}")
            finally:
                del raw
                try:
                    del result
                except NameError:
                    pass
                gc.collect()

        out_fh.write("\n]}\n")

    print(f"   -> Final JSON saved → {EXTRACTED_JSON}")
    return EXTRACTED_JSON


# ---------------------------------------------------------------------------
# STEP 6 — Export to Word document
# ---------------------------------------------------------------------------

def step_export_docx(extracted_json_path: str) -> None:
    print("\n=== STEP 6: Exporting to Word Document ===")
    create_docx_from_json(extracted_json_path, OUTPUT_DOCX)
    print(f"   -> Document saved → {OUTPUT_DOCX}")


# ---------------------------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------------------------

async def run_pipeline():
    _setup_dirs()

    with open("project_description.txt", "r", encoding="utf-8") as f:
        question_prompt = f.read()

    print(question_prompt)

    # Step 1: Extract metadata (Groq)
    extracted_meta, links = step_extract_metadata(question_prompt)
    del question_prompt
    gc.collect()

    # Step 2: Crawl links → disk
    crawl_manifest = await step_crawl_links(links)
    del links
    gc.collect()

    # Step 3: Tavily search → disk
    tavily_manifest = step_tavily_search(extracted_meta.tavily_search_prompts)
    del extracted_meta
    gc.collect()

    # Step 4: Summarise each source → disk
    summary_manifest = step_summarise_per_area(crawl_manifest, tavily_manifest)
    del crawl_manifest, tavily_manifest
    gc.collect()

    # Step 5: Generate final draft → streamed to disk
    extracted_json_path = step_generate_final_draft(summary_manifest)
    del summary_manifest
    gc.collect()

    # Step 6: Export docx
    step_export_docx(extracted_json_path)

    print("\n✅ Pipeline complete! See", OUTPUT_DOCX)


if __name__ == "__main__":
    asyncio.run(run_pipeline())
