# from webcrawler.crawl import start_async_crawl
# import json 

# def read_urls_from_json(file_path):
#     with open(file_path, "r") as f:
#         urls = json.load(f)
#     return urls



# if __name__ == "__main__":
#     data = read_urls_from_json("data/webpages.json")
#     md = 10
    

#     raw_context = {}
#     context_file_path = "context/context.md"
#     for key in data.keys():
#         raw_context[key] = start_async_crawl(data[key], md)

#     print(raw_context)

#     with open(context_file_path, "w") as f:
#         json.dump(raw_context, f)
#     print(f"Raw context saved to {context_file_path}")
    

# pyrefly: ignore [missing-import]
from helpers.gemini_helper import gemini_api_call_for_coding_standard_doc
from pydantic_models.models import DocumentContent
import json
import time

def chunk_string(text, chunk_size):
    """Splits a large string into smaller chunks of chunk_size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

if __name__ == "__main__":
    context_file_path = "context/context.md"
    try:
        with open(context_file_path, "r") as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Error: {context_file_path} not found. Please run the crawler first.")
        exit(1)

    print(f"Total characters to process: {len(raw_text)}")
    
    # 500,000 characters is roughly 125,000 tokens, which sits safely below the 250k token/min limit.
    chunk_size = 100000 
    chunks = chunk_string(raw_text, chunk_size)
    all_sections = []
    
    for i, chunk in enumerate(chunks):
        print(f"\n--- Processing chunk {i+1} of {len(chunks)} ---")
        try:
            # Send the chunk to Gemini
            json_result_str = gemini_api_call_for_coding_standard_doc(chunk, DocumentContent)
            
            # The API returns a JSON string, which we can parse with Pydantic
            structured_data = DocumentContent.model_validate_json(json_result_str)
            all_sections.extend(structured_data.sections)
            
            # Sleep to avoid hitting the 250k Tokens-Per-Minute limit if not the last chunk
            if i < len(chunks) - 1:
                print("Sleeping for 60 seconds to respect API rate limits...")
                time.sleep(60) 
            
        except Exception as e:
            print(f"Error on chunk {i+1}: {e}")
            
    # Reassemble the final structured document
    final_document = DocumentContent(sections=all_sections)
    print(f"\nTotal Sections Extracted: {len(final_document.sections)}")
    
    # Save the output to a file
    output_file = "coding_standards_extracted.json"
    with open(output_file, "w") as f:
        # Pydantic v2 uses model_dump_json
        f.write(final_document.model_dump_json(indent=4))
        
    print(f"Successfully saved structured coding standards to {output_file}")