import json
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_docx_from_json(json_path, output_path):
    # Load the JSON data
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Create a new Document
    doc = Document()
    
    # Optional: Set a main title if the JSON doesn't start with one
    # doc.add_heading('Coding Standards Document', 0)

    for section in data.get('sections', []):
        header_type = section.get('header_type', 'p')
        header_text = section.get('header_text', '')
        text_content = section.get('text', '')

        # Map header types to docx levels and set sizes
        if header_type == 'h1':
            h = doc.add_heading(header_text, level=1)
            for run in h.runs:
                run.font.size = Pt(11)
        elif header_type == 'h2':
            h = doc.add_heading(header_text, level=2)
            for run in h.runs:
                run.font.size = Pt(10)
        elif header_type == 'h3':
            h = doc.add_heading(header_text, level=3)
            for run in h.runs:
                run.font.size = Pt(10)
        elif header_type == 'h4':
            h = doc.add_heading(header_text, level=4)
            for run in h.runs:
                run.font.size = Pt(10)
        else:
            # For p or others, just add a bold line or similar if header exists
            if header_text:
                p = doc.add_paragraph()
                p.add_run(header_text).bold = True
        
        # Add the main text content
        if text_content:
            # Split text into lines to detect bullet points
            lines = text_content.split('\n')
            for line in lines:
                clean_line = line.strip()
                if not clean_line:
                    continue
                
                if clean_line.startswith('*'):
                    # Add as a bullet point
                    bullet_text = clean_line[1:].strip()
                    p = doc.add_paragraph(bullet_text, style='List Bullet')
                    # Set font size to 10pt
                    for run in p.runs:
                        run.font.size = Pt(10)
                else:
                    # Add as a normal paragraph
                    p = doc.add_paragraph(clean_line)
                    # Set font size to 10pt
                    for run in p.runs:
                        run.font.size = Pt(10)

    # Save the document
    doc.save(output_path)
    print(f"Document saved successfully to {output_path}")

