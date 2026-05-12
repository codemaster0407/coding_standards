import os
import json
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)

# ---------------------------------------------------------------------------
# TPM budget: limit 12,000 tokens/min (on_demand tier, llama-3.3-70b-versatile)
#   ~1,250 tokens input  (5,000 chars @ 4 chars/token)
#   ~2,048 tokens output
#   ~3,300 tokens/call  →  sleep 20 s  →  ~3 calls/min  →  ~9,900 tokens/min
# ---------------------------------------------------------------------------
GROQ_CHUNK_SIZE     = 5_000   # characters per chunk sent to the API
MAX_OUTPUT_TOKENS   = 2_048   # max tokens the model may return per call
SLEEP_BETWEEN_CALLS = 20      # seconds to wait after every Groq API call


def chunk_string(text: str, chunk_size: int = GROQ_CHUNK_SIZE) -> list[str]:
    """Split *text* into chunks of at most *chunk_size* characters."""
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


def groq_api_call(prompt: str, raw_text: str, pydantic_class=None) -> any:
    """
    Calls llama-3.3-70b-versatile via Groq.

    Modes
    -----
    pydantic_class provided  → JSON mode; returns a validated Pydantic instance.
    pydantic_class is None   → Plain-text mode; returns a raw string.

    A mandatory sleep of SLEEP_BETWEEN_CALLS seconds is enforced after every
    successful or failed call to respect the 12,000 TPM rate limit.
    """
    full_prompt = f"{prompt}\n\nRaw Text:\n{raw_text}" if raw_text else prompt

    try:
        if pydantic_class:
            # ---- Structured JSON output ----
            schema = pydantic_class.model_json_schema()
            system_msg = (
                "You are a technical data extractor. "
                f"Output ONLY valid JSON matching this schema: {json.dumps(schema)}"
            )
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user",   "content": full_prompt},
                ],
                temperature=0.1,
                max_completion_tokens=MAX_OUTPUT_TOKENS,
                top_p=1,
                response_format={"type": "json_object"},
                stop=None,
            )
            content = completion.choices[0].message.content
            return pydantic_class.model_validate_json(content)

        else:
            # ---- Plain-text output (summarisation / draft) ----
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a senior engineering technical writer. "
                            "Follow the user's instructions precisely and output "
                            "well-structured plain text."
                        ),
                    },
                    {"role": "user", "content": full_prompt},
                ],
                temperature=0.3,
                max_completion_tokens=MAX_OUTPUT_TOKENS,
                top_p=1,
                stop=None,
            )
            return completion.choices[0].message.content

    finally:
        # Always sleep — even on error — so the next call isn't rate-limited
        print(f"   [rate-limit] sleeping {SLEEP_BETWEEN_CALLS}s …")
        time.sleep(SLEEP_BETWEEN_CALLS)
