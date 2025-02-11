import pytesseract
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

def test_tesseract():
    # Set Tesseract path
    tesseract_cmd = os.getenv('TESSERACT_CMD')
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
    try:
        # Print Tesseract version
        print("Tesseract Version:", pytesseract.get_tesseract_version())
        print("Tesseract Path:", pytesseract.pytesseract.tesseract_cmd)
        print("\nTesseract is properly installed and configured!")
        
    except Exception as e:
        print("Error:", str(e))
        print("\nPlease check your Tesseract installation and path configuration.")

if __name__ == "__main__":
    test_tesseract() 