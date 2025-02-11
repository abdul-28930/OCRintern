from ocr.preprocessor import preprocess_image
from ocr.extractor import FormExtractor
from database.db_handler import DatabaseHandler
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging with more detail
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_form(image_path: str) -> None:
    """Process a form image and store the data"""
    try:
        # Validate image path
        if not os.path.isabs(image_path):
            # Convert relative path to absolute path
            image_path = os.path.abspath(image_path)
            
        logging.info(f"Processing image: {image_path}")
        
        # Initialize components
        db_handler = DatabaseHandler()
        extractor = FormExtractor()
        
        # Process image
        preprocessed_image = preprocess_image(image_path)
        logging.info("Image preprocessing completed")
        
        form_data = extractor.extract_form_data(preprocessed_image)
        logging.info("Data extraction completed")
        
        # Store in database
        assessment_id = db_handler.store_form_data(form_data)
        logging.info(f"Successfully stored assessment with ID: {assessment_id}")
        
    except FileNotFoundError as e:
        logging.error(f"File not found: {str(e)}")
        print(f"\nError: The image file was not found. Please check the path: {image_path}")
        raise
    except ValueError as e:
        logging.error(f"Invalid image or processing error: {str(e)}")
        print(f"\nError: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        print(f"\nAn unexpected error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("\nUsage: python main.py <path_to_form_image>")
        print("Example: python main.py sample_form.jpg")
        print("\nSupported image formats: .jpg, .jpeg, .png, .tiff")
        sys.exit(1)
        
    image_path = sys.argv[1]
    
    # Validate file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.tiff']
    file_extension = os.path.splitext(image_path)[1].lower()
    
    if file_extension not in valid_extensions:
        print(f"\nError: Unsupported file format. Please use one of: {', '.join(valid_extensions)}")
        sys.exit(1)
        
    try:
        process_form(image_path)
    except Exception:
        sys.exit(1) 