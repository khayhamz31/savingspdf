import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF file.
    Returns a single string containing all pages.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text