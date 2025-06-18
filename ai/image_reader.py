from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# ✅ Set the path to the installed Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert('L')  # Convert to grayscale
        image = image.filter(ImageFilter.SHARPEN)  # Sharpen text
        image = ImageEnhance.Contrast(image).enhance(2)  # Increase contrast

        text = pytesseract.image_to_string(image, lang='eng')  # Use English OCR
        return text.strip()
    except Exception as e:
        return f"Error processing image: {e}"
