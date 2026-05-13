import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from helpers.docx_reader import read_docx


# Download necessary NLTK data (only needed once)
for resource in ['punkt', 'punkt_tab']:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)

def calculate_metrics(reference_text, candidate_text):
    """
    Calculates BLEU and ROUGE scores between a reference and candidate text.
    """
    # 1. ROUGE Scores
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_results = scorer.score(reference_text, candidate_text)
    
    # 2. BLEU Score
    ref_tokens = nltk.word_tokenize(reference_text.lower())
    cand_tokens = nltk.word_tokenize(candidate_text.lower())
    
    smoothie = SmoothingFunction().method1
    bleu_score = sentence_bleu([ref_tokens], cand_tokens, smoothing_function=smoothie)
    
    return {
        "bleu": bleu_score,
        "rouge1": rouge_results['rouge1'].fmeasure,
        "rouge2": rouge_results['rouge2'].fmeasure,
        "rougeL": rouge_results['rougeL'].fmeasure
    }

def evaluate_docs(ref_path, cand_path):
    reference = read_docx(ref_path)
    candidate = read_docx(cand_path)
    
    if not reference or not candidate:
        print(f"Error: Ensure files exist at {ref_path} and {cand_path}")
        return

    results = calculate_metrics(reference, candidate)
    
    print("\nEvaluation Results:")
    print(f"BLEU Score: {results['bleu']:.4f}")
    print(f"ROUGE-1:    {results['rouge1']:.4f}")
    print(f"ROUGE-2:    {results['rouge2']:.4f}")
    print(f"ROUGE-L:    {results['rougeL']:.4f}")

