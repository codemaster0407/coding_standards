import os
import json
import time
import asyncio
from dotenv import load_dotenv

# Import local helpers
from helpers.tavily_search import perform_tavily_search
from webcrawler.crawl import start_async_crawl, main as crawl_single_url
from helpers.gemini_helper import gemini_api_call_for_coding_standard_doc, chunk_string
from pydantic_models.models import DocumentContent
from helpers.json_to_docx import create_docx_from_json

load_dotenv()

async def run_consolidated_pipeline():
    # 1. SETUP DIRECTORIES
    os.makedirs("context", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    context_file_path = "context/context.md"
    
    # Clear previous context if it exists
    if os.path.exists(context_file_path):
        os.remove(context_file_path)

    # 2. PERFORM TAVILY SEARCH
    print("\n--- STEP 1: Performing Tavily Search ---")
    with open("data/tavily_queries.json", "r") as f:
        search_queries = json.load(f)

    search_context = {}
    for query_item in search_queries:
        key = list(query_item.keys())[0]
        query_text = query_item[key]
        print(f"Searching for: {key}...")
        results = perform_tavily_search(query_text)
        search_context[key] = results 

    tavily_json_path = 'context/tavily_context.json'
    with open(tavily_json_path, 'w') as f:
        json.dump(search_context, f, indent=4)
    print(f"Saved search results to {tavily_json_path}")

    # 3. SCRAPE SEARCH RESULTS
    print("\n--- STEP 2: Scraping URLs from Search Results ---")
    scraped_content = []
    for category in search_context.values():
        for result in category.get('results', []):
            url = result['url']
            print(f"Scraping result URL: {url}")
            try:
                # Using the single URL crawl helper from your crawler
                content = await crawl_single_url(url)
                scraped_content.append(f"## Source: {url}\n\n{content}\n\n")
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

    # 4. SCRAPE USER-PROVIDED URLS
    print("\n--- STEP 3: Scraping User-Provided URLs ---")
    with open("data/webpages.json", "r") as f:
        user_urls = json.load(f)

    for name, url in user_urls.items():
        print(f"Crawling user URL: {name} ({url})")
        # Using your recursive async crawl for these primary sources
        content = start_async_crawl(url, md=5) # Reduced depth for speed
        scraped_content.append(f"## Primary Source: {name}\n\n{content}\n\n")

    # Save all aggregated content to context.md
    with open(context_file_path, "w") as f:
        f.writelines(scraped_content)
    print(f"Aggregated content saved to {context_file_path}")

    # 5. GEMINI EXTRACTION
    print("\n--- STEP 4: Extracting Structured Data with Gemini ---")
    with open(context_file_path, "r") as f:
        raw_text = f.read()

    print(f"Total characters to process: {len(raw_text)}")
    chunk_size = 100000 
    chunks = chunk_string(raw_text, chunk_size)
    all_sections = []
    
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1} of {len(chunks)}...")
        try:
            json_result_str = gemini_api_call_for_coding_standard_doc(chunk, DocumentContent)
            structured_data = DocumentContent.model_validate_json(json_result_str)
            all_sections.extend(structured_data.sections)
            
            if i < len(chunks) - 1:
                print("Rate limit cooling (10s)...")
                time.sleep(10) # Reduced sleep for Gemini 2.5 Flash
        except Exception as e:
            print(f"Error on chunk {i+1}: {e}")

    final_document = DocumentContent(sections=all_sections)
    extracted_json_path = "context/coding_standards_extracted.json"
    with open(extracted_json_path, "w") as f:
        f.write(final_document.model_dump_json(indent=4))
    print(f"Extracted data saved to {extracted_json_path}")

    # 6. GENERATE DOCX
    print("\n--- STEP 5: Generating Word Document ---")
    output_docx = 'Coding_Standards.docx'
    create_docx_from_json(extracted_json_path, output_docx)
    print(f"Final document created: {output_docx}")

if __name__ == "__main__":
    asyncio.run(run_consolidated_pipeline())
