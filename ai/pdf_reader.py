import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"
