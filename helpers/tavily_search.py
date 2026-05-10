import os
from tavily import TavilyClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


api_key = os.getenv("TAVILY_KEY")
    
if not api_key:
    print("Error: TAVILY_KEY not found in .env file.")
    exit(1)

# Initialize the Tavily client
tavily = TavilyClient(api_key=api_key)

def perform_tavily_search(query: str):
    """
    Performs a web search using Tavily and returns the results.
    """
    # Get API key from environment


    print(f"Searching for: {query}...")
    
    # Execute the search
    # search_depth="advanced" includes more detailed content
    # max_results determines how many links to return
    response = tavily.search(
        query=query, 
        search_depth="advanced", 
        max_results=5
    )

    return response

