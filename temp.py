from helpers import url_regex
from helpers import groq_helper as grhelp
from pydantic_models.models import TechStackData
from prompts.gemini_prompts import DATA_EXTRACTION_PROMPT

question_prompt = ""

with open('project_description.txt', 'r') as f:
    question_prompt = f.read()

print(question_prompt)

links_extracted = url_regex.extract_https_urls(question_prompt)
print(links_extracted)

data = grhelp.groq_api_call(
    raw_text=question_prompt,
    pydantic_class=TechStackData,
    prompt=DATA_EXTRACTION_PROMPT,
)

print("\n--- Extracted Tech Stack ---")
print(data.techstack)
print("\n--- Tavily Search Prompts ---")
for p in data.tavily_search_prompts:
    print(f"- {p}")
