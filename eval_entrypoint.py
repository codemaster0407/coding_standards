from evaluation.evaluate import evaluate_docs
from evaluation.language_model_eval import run_llm_evaluation

evaluate_docs('data/reference_files/Coding_Standards.docx', 
                'output/Coding_Standards.docx')

run_llm_evaluation()