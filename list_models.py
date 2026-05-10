import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def list_gemini_models():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file.")
        return

    # Initialize the client
    client = genai.Client(api_key=api_key)

    print("Fetching available models...")
    try:
        # List all models
        models = client.models.list()
        
        print(f"{'Model Name':<40} | {'Supported Methods'}")
        print("-" * 70)
        
        for model in models:
            # Print the entire model object to see available attributes or just the name
            print(model)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_gemini_models()
