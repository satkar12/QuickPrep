from ai.pdf_reader import extract_text_from_pdf
from ai.summarizer import summarize_text

def test_summary():
    text = extract_text_from_pdf('../sample.pdf')
    summary = summarize_text(text)
    assert len(summary) > 0
    print("Test passed. Summary length:", len(summary))
