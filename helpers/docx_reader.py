from docx import Document

def read_docx(file_path):
    """
    Reads all text from a .docx file and returns it as a single string,
    preserving paragraph breaks.
    """
    try:
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():  # Only add non-empty paragraphs
                full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error reading docx file {file_path}: {e}")
        return ""
