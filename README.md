# Engineering Coding Standards Automation

This project automates the process of extracting, structuring, and generating formal engineering coding standards for a product agency. It uses a combination of web crawling and Generative AI (Google Gemini) to transform raw documentation into a professional Word document.

## Architecture

![GenAI Architecture Diagram](GenAI%20.drawio.png)

The pipeline consists of the following stages:
1.  **Task Prompting:** Defining the scope and technical requirements.
2.  **Web Crawling:** Extracting links and documentation from specified sources.
3.  **Context Creation:** Aggregating raw text from multiple sources into a unified context.
4.  **Data Chunking:** Splitting large contexts to fit within model token limits.
5.  **GenAI Processing:** Using **Gemini 2.5 Flash** to perform structured extraction based on Pydantic models.
6.  **Document Generation:** Converting the structured JSON output into a professional `.docx` file using Python.

## Getting Started

### Prerequisites
- Python 3.10+
- Google GenAI API Key
- Tavily API Key (for web search)

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file:
   ```env
   GEMINI_API_KEY=your_api_key
   TAVILY_KEY=your_tavily_key
   ```

### Running the Pipeline
To run the extraction process:
```bash
python temp.py
```
To generate the Word document:
```bash
python json_to_docx.py
```

## Tech Stack
- **AI:** Google Gemini (2.5 Flash)
- **Crawler:** Custom Python-based crawler
- **Data Validation:** Pydantic
- **Document Output:** python-docx
