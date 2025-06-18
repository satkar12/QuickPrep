from ai.pdf_reader import extract_text_from_pdf
from ai.image_reader import extract_text_from_image
from ai.summarizer import summarize_text

def main():
    # Choose one
    input_type = 'image'  # or 'pdf'
    input_path = 'page.png'  # or 'sample.pdf'

    if input_type == 'pdf':
        print("[INFO] Reading from PDF...")
        text = extract_text_from_pdf(input_path)
    else:
        print("[INFO] Reading from Image...")
        text = extract_text_from_image(input_path)

    if "Error" in text or len(text.strip()) == 0:
        print("[ERROR] No readable text found.")
        return

    print("[INFO] Summarizing...")
    summary = summarize_text(text)
    print("\n=== Summary ===\n", summary)

if __name__ == '__main__':
    main()
