import os
import PyPDF2

def extract_text_from_pdf(pdf_path: str) -> str:
    if not os.path.isfile(pdf_path):
        raise ValueError("Invalid file path")

    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("Not a PDF file")

    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text
