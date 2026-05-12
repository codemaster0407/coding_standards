import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()


def chunk_string(text, chunk_size):
    """Splits a large string into smaller chunks of chunk_size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


def gemini_api_call(raw_text: str, pydantic_class, prompt: str) -> str:
    """
    Calls Gemini for structured extraction or plain text generation.
    - If pydantic_class is provided: returns JSON string matching that schema.
    - If pydantic_class is None: returns a plain text response.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please ensure it is in your .env file.")

    client = genai.Client(api_key=api_key)

    # Append raw text to prompt if provided
    if raw_text:
        prompt = prompt + "\n" + raw_text

    print(f"   -> Sending to Gemini ({'structured' if pydantic_class else 'plain text'})...")

    if pydantic_class:
        # Structured JSON output mode
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=pydantic_class,
                temperature=0.0,
            ),
        )
    else:
        # Plain text output mode (used for summarisation)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
            ),
        )

    return response.text
