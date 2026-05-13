# Engineering Coding Standards Automation

This project automates the creation of professional engineering coding standards for product agencies. It uses a **Map-Reduce architecture** to process large volumes of technical documentation and a **multi-stage evaluation pipeline** to ensure compliance with client deliverables.

## 🏗️ Pipeline Architecture

The system follows a three-stage automated workflow:

### 1. Discovery & Ingestion
- **Tavily Search:** Identifies industry best practices based on configurable queries in `data/tavily_queries.json`.
- **Async Crawling:** Scrapes documentation from search results and primary sources listed in `data/webpages.json`.

### 2. Map-Reduce Synthesis
- **Map Phase (Summarization):** Large datasets are chunked and summarized by **Gemini 1.5 Flash**. The model uses the `deliverables.txt` rubric as a filter to extract only relevant technical patterns.
- **Reduce Phase (Generation):** Summaries are synthesized into a structured 1200-word document. The model ensures mandatory sections (Governance, Rollout, Tech Stack) are prioritized.
- **Document Assembly:** The final structured JSON is converted into a professional Word document (`output/Coding_Standards.docx`) with optimized formatting (11pt headers, 10pt body).

### 3. Automated Evaluation (`eval_entrypoint.py`)
This project includes a rigorous evaluation suite to verify document quality:
- **Statistical Metrics:** Calculates **BLEU** and **ROUGE** scores comparing the generated standards against a reference document. Results are saved to `output/nltk-metrics.json`.
- **LLM Quality Audit:** Uses **Gemini 1.5 Pro** to perform a deep-dive audit against a 132-item rubric. It produces a categorized compliance report in `output/client_compliance_audit.md` with an overall score and gap analysis.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- API Keys: Google Gemini, Tavily

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your `.env`:
   ```env
   GEMINI_API_KEY=your_key
   TAVILY_KEY=your_key
   ```

### Execution
Run the full generation pipeline:
```bash
python main.py
```

Run the quality evaluation:
```bash
python eval_entrypoint.py
```

## 📊 Outputs
- `output/Coding_Standards.docx`: The final professional document.
- `output/nltk-metrics.json`: Statistical comparison data.
- `output/client_compliance_audit.md`: Detailed LLM audit report.

## 🛠️ Tech Stack
- **AI Models:** Gemini 2.0 Flash (Generation), Gemini 2.5 Pro (Auditing)
- **Data Validation:** Pydantic
- **Search:** Tavily API
- **NLP:** NLTK, ROUGE-Score
- **Document Processing:** python-docx
