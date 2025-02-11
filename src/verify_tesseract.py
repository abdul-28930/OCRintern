import os
import sys
from dotenv import load_dotenv
import pytesseract
from PIL import Image

def verify_installation():
    # Load environment variables
    load_dotenv()
    
    # Print Python version and working directory
    print(f"Python Version: {sys.version}")
    print(f"Working Directory: {os.getcwd()}")
    
    # Check Tesseract path
    tesseract_cmd = os.getenv('TESSERACT_CMD')
    print(f"\nTesseract Path from .env: {tesseract_cmd}")
    
    # Check if file exists
    if tesseract_cmd and os.path.exists(tesseract_cmd):
        print("✓ Tesseract executable found")
    else:
        print("✗ Tesseract executable not found at specified path")
    
    # Set Tesseract path
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
    try:
        # Try to get Tesseract version
        version = pytesseract.get_tesseract_version()
        print(f"\n✓ Tesseract is working! Version: {version}")
        
        # Try basic OCR on a test string
        test_image = Image.new('RGB', (100, 30), color='white')
        test_text = pytesseract.image_to_string(test_image)
        print("✓ OCR test successful")
        
    except Exception as e:
        print(f"\n✗ Error testing Tesseract: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Verify Tesseract is installed correctly")
        print("2. Check if the path in .env is correct")
        print("3. Try running 'tesseract --version' in Command Prompt")
        print("4. Make sure Tesseract is added to system PATH")

if __name__ == "__main__":
    verify_installation() 