import fitz  # PyMuPDF
# importing pymupdf didnt worked on local system, so i used google colab.

def extract_pdf_text(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text
extract_pdf_text('llm.pdf')