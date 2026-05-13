import os
import json
import time
import asyncio
from dotenv import load_dotenv

# Import local helpers
from helpers.tavily_search import perform_tavily_search
from webcrawler.crawl import start_async_crawl, main as crawl_single_url
from helpers.gemini_helper import (
    gemini_api_call_for_coding_standard_doc,
    gemini_summarise_chunk,
    gemini_generate_final_document,
    chunk_string,
)
from pydantic_models.models import DocumentContent
from helpers.json_to_docx import create_docx_from_json

load_dotenv()

async def run_consolidated_pipeline():
    # # 1. SETUP DIRECTORIES
    os.makedirs("context", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    context_file_path = "context/context.md"
    
    # # Clear previous context if it exists
    # if os.path.exists(context_file_path):
    #     os.remove(context_file_path)

    # # 2. PERFORM TAVILY SEARCH
    # print("\n--- STEP 1: Performing Tavily Search ---")
    # with open("data/tavily_queries.json", "r") as f:
    #     search_queries = json.load(f)

    # search_context = {}
    # for query_item in search_queries:
    #     key = list(query_item.keys())[0]
    #     query_text = query_item[key]
    #     print(f"Searching for: {key}...")
    #     results = perform_tavily_search(query_text)
    #     search_context[key] = results 

    # tavily_json_path = 'context/tavily_context.json'
    # with open(tavily_json_path, 'w') as f:
    #     json.dump(search_context, f, indent=4)
    # print(f"Saved search results to {tavily_json_path}")

    # # 3. SCRAPE SEARCH RESULTS
    # print("\n--- STEP 2: Scraping URLs from Search Results ---")
    # scraped_content = []
    # for category in search_context.values():
    #     for result in category.get('results', []):
    #         url = result['url']
    #         print(f"Scraping result URL: {url}")
    #         try:
    #             # Using the single URL crawl helper from your crawler
    #             content = await crawl_single_url(url)
    #             scraped_content.append(f"## Source: {url}\n\n{content}\n\n")
    #         except Exception as e:
    #             print(f"Failed to scrape {url}: {e}")

    # # 4. SCRAPE USER-PROVIDED URLS
    # print("\n--- STEP 3: Scraping User-Provided URLs ---")
    # with open("data/webpages.json", "r") as f:
    #     user_urls = json.load(f)

    # for name, url in user_urls.items():
    #     print(f"Crawling user URL: {name} ({url})")
    #     # Using your recursive async crawl for these primary sources
    #     content = start_async_crawl(url, md=5) # Reduced depth for speed
    #     scraped_content.append(f"## Primary Source: {name}\n\n{content}\n\n")

    # # Save all aggregated content to context.md
    # with open(context_file_path, "w") as f:
    #     f.writelines(scraped_content)
    # print(f"Aggregated content saved to {context_file_path}")

    # 5. LOAD RUBRIC
    rubric = ""
    rubric_path = "data/reference_files/deliverables.txt"
    if os.path.exists(rubric_path):
        with open(rubric_path, "r") as f:
            rubric = f.read()
    else:
        print(f"[WARN] Rubric not found at {rubric_path}. Proceeding without strict filtering.")

    # # 6. GEMINI EXTRACTION — Map-Reduce pipeline
    # print("\n--- STEP 4a: Summarising Chunks (MAP phase) ---")
    # with open(context_file_path, "r") as f:
    #     raw_text = f.read()

    # print(f"Total characters to process: {len(raw_text):,}")
    # chunk_size = 100000
    # chunks = chunk_string(raw_text, chunk_size)
    # print(f"Total chunks: {len(chunks)}")

    # chunk_summaries = []
    # for i, chunk in enumerate(chunks):
    #     print(f"  Summarising chunk {i+1}/{len(chunks)}...")
    #     try:
    #         summary = gemini_summarise_chunk(chunk, chunk_index=i+1, total_chunks=len(chunks), rubric_text=rubric)
    #         chunk_summaries.append(f"### Summary of chunk {i+1}\n{summary}")
    #     except Exception as e:
    #         print(f"  [WARN] Failed to summarise chunk {i+1}: {e}")
    #         chunk_summaries.append(f"### Summary of chunk {i+1}\n(summarisation failed: {e})")

    #     if i < len(chunks) - 1:
    #         print("  Rate-limit cooldown (10s)...")
    #         time.sleep(10)

    # # Persist summaries so the final-doc step can be re-run independently
    # summaries_path = "context/chunk_summaries.md"
    # summaries_text = "\n\n".join(chunk_summaries)
    # with open(summaries_path, "w") as f:
    #     f.write(summaries_text)
    # print(f"Chunk summaries saved to {summaries_path} ({len(summaries_text):,} chars)")

    
    # summaries_text = ""
    # with open('context/chunk_summaries.md', 'r') as f:
    #     summaries_text = f.read()
    # print("\n--- STEP 4b: Generating Final 1200-Word Document (REDUCE phase) ---")
    # # print(f"  Sending {len(summaries_text)} summaries to Gemini for final generation...")
    # try:
    #     json_result_str = gemini_generate_final_document(summaries_text, DocumentContent, rubric_text=rubric)
    #     final_document = DocumentContent.model_validate_json(json_result_str)
    # except Exception as e:
    #     print(f"[ERROR] Final document generation failed: {e}")
    #     raise

    extracted_json_path = "context/coding_standards_extracted.json"
    # with open(extracted_json_path, "w") as f:
    #     f.write(final_document.model_dump_json(indent=4))
    # print(f"Extracted data saved to {extracted_json_path}")

    # 6. GENERATE DOCX
    print("\n--- STEP 5: Generating Word Document ---")
    output_docx = 'output/Coding_Standards.docx'
    create_docx_from_json(extracted_json_path, output_docx)
    print(f"Final document created: {output_docx}")

if __name__ == "__main__":
    asyncio.run(run_consolidated_pipeline())
