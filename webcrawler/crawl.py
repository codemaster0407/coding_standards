import asyncio
from crawl4ai import *
from helpers.url_regex import extract_https_urls

async def main(url, max_depth = 1):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            max_depth = max_depth
        )
    return str(result.markdown)


import time

def start_async_crawl(initial_url, md=100, max_time=100):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    queue = [initial_url]
    visited = set()
    all_results = []
    
    start_time = time.time()
    count = 0
    while queue and count < md:

        current_url = queue.pop(0)
        if current_url in visited:
            continue
            
        print(f"Crawling {count + 1}/{md}: {current_url}")
        try:
            # We run the crawl for the current url
            result = loop.run_until_complete(main(current_url, max_depth=1))
            all_results.append(result)
            visited.add(current_url)
            
            # Extract new links and add them to the queue
            urls = extract_https_urls(result)
            for u in urls:
                if u not in visited and u not in queue:
                    queue.append(u)
                    
            count += 1
        except Exception as e:
            print(f"Error crawling {current_url}: {e}")

    loop.close()
    return "\n\n---\n\n".join(all_results)
    

