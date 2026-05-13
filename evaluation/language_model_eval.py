import os
from helpers.gemini_helper import gemini_text_evaluator
from helpers.docx_reader import read_docx

def run_llm_evaluation():
    # 1. Define paths
    deliverables_path = "data/reference_files/deliverables.txt"
    generated_doc_path = "output/Coding_Standards.docx"
    output_report_path = "evaluation/client_compliance_audit.md"

    print(f"--- Starting LLM-based Evaluation ---")
    
    # 2. Read Client Deliverables Rubric
    if not os.path.exists(deliverables_path):
        print(f"[ERROR] Deliverables file not found at {deliverables_path}")
        return
    
    with open(deliverables_path, 'r') as f:
        rubric = f.read()
    print(f"-> Loaded client deliverables rubric.")

    # 3. Read Generated Document
    if not os.path.exists(generated_doc_path):
        print(f"[ERROR] Generated document not found at {generated_doc_path}")
        return
    
    content = read_docx(generated_doc_path)
    print(f"-> Loaded generated document ({len(content.split())} words).")

    # 4. Perform Evaluation
    print("-> Sending to Gemini for quality audit... (this may take 20-30s)")
    try:
        report = gemini_text_evaluator(rubric, content)
        
        # 5. Save the report
        with open(output_report_path, 'w') as f:
            f.write(report)
        
        print(f"\n--- AUDIT COMPLETE ---")
        print(f"Report saved to: {output_report_path}")
        print("\nSummary of results:")
        # Print just the first few lines of the report (usually includes the score)
        print("\n".join(report.split('\n')[:5]))
        
    except Exception as e:
        print(f"[ERROR] Evaluation failed: {e}")

# if __name__ == "__main__":
#     run_llm_evaluation()