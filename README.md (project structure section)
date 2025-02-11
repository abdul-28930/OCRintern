# OCR-Based Functional Assessment Tool

## Overview
This project extracts text from scanned forms using OCR (Optical Character Recognition) and stores structured data in a Supabase database.

## Installation

### Dependencies
Ensure you have the required dependencies installed. Use the following command to install them:
```bash
pip install -r requirements.txt
```

**Dependencies:**
```
# OCR dependencies
pytesseract==0.3.10
opencv-python==4.8.0.74
numpy==1.24.3

# Database dependencies
supabase==1.0.3

# Other utilities
python-dotenv==1.0.0
```

### Environment Variables
Create a `.env` file and set the following values:
```
SUPABASE_URL=https://ihmxjlvpceaxxokoaecc.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
TESSERACT_CMD=C:\Users\abdul\AppData\Local\Programs\Tesseract-OCR\tesseract.exe
```

## Usage
To process an image file and extract form data, run the following command:
```bash
python src/main.py path/to/image.png
```
Example:
```bash
python src/main.py C:\Users\abdul\Documents\OCRintern\ocr.png
```

### Process Flow
1. **Image Preprocessing:** The tool enhances the image for better OCR results.
2. **OCR Extraction:** Extracts text from the image using Tesseract OCR.
3. **Data Parsing:** Converts the raw OCR text into structured form data.
4. **Database Storage:** Saves the extracted data to Supabase.

## Database Schema
### Table: `patient_assessments`
| Column                | Type     | Constraints        |
|----------------------|---------|------------------|
| id                   | UUID    | Primary Key       |
| created_at           | TIMESTAMP | Auto-generated    |
| patient_name         | TEXT    | NOT NULL         |
| dob                  | TEXT    | Nullable         |
| date                | TEXT    | NOT NULL         |
| injection           | BOOLEAN | Default: False   |
| exercise_therapy    | BOOLEAN | Default: False   |
| difficulty_ratings  | JSONB   | Stores ratings   |
| patient_changes     | JSONB   | Stores changes   |
| pain_symptoms       | JSONB   | Stores symptoms  |
| medical_assistant_data | JSONB | Stores MA notes  |
| raw_ocr_data        | TEXT    | Raw OCR output   |

## Error Handling
If a required field (e.g., `patient_name`) is missing, the insertion to the database will fail with an error like:
```
ERROR - null value in column "patient_name" of relation "patient_assessments" violates not-null constraint
```
To prevent this, ensure that `patient_name` is always extracted correctly. In case of failure, a fallback mechanism assigns a default name:
```
'patient_name': 'Patient_YYYYMMDD_HHMMSS'
```

## Example Logs
```
2025-02-11 12:28:01,222 - INFO - Processing image: C:\Users\abdul\Documents\OCRintern\ocr.png
2025-02-11 12:28:01,930 - INFO - Successfully connected to Supabase
2025-02-11 12:28:01,931 - INFO - Using Tesseract at: C:\Users\abdul\AppData\Local\Programs\Tesseract-OCR\tesseract.exe
2025-02-11 12:28:02,126 - INFO - Image preprocessing completed
2025-02-11 12:28:02,495 - INFO - Raw OCR Text: (extracted data)
2025-02-11 12:28:02,506 - INFO - Data extraction completed
2025-02-11 12:28:02,756 - INFO - Successfully stored assessment with ID: bdbb2f33-b0db-490c-a6b0-d91cf12271df
```
## Project Structure

medical-form-ocr/
├── src/
│   ├── ocr/
│   │   ├── preprocessor.py    # Image preprocessing
│   │   └── extractor.py       # OCR data extraction
│   ├── database/
│   │   ├── models.py          # Database models
│   │   └── db_handler.py      # Database operations
│   ├── main.py               # Main application
│   ├── test_db.py           # Database tests
│   ├── test_ocr.py          # OCR tests
│   └── verify_tesseract.py  # Installation verification
├── sql/
│   └── schema.sql           # Database schema
├── samples/
│   ├── sample_output.json   # Example JSON output
│   └── sample_form.jpg      # Example form image
├── .env                     # Environment variables
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
└── README.md              # Documentation 

## Future Improvements
- Enhance OCR accuracy using AI-based text correction.
- Improve parsing for better structured data extraction.
- Add a UI for manual verification and corrections.

## License
This project is licensed under the MIT License.

