from supabase import create_client, Client
from typing import Dict, Any, Optional, List
from datetime import datetime
import os
import logging

class DatabaseHandler:
    def __init__(self):
        """Initialize Supabase client"""
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        
        if not self.supabase_url or not self.supabase_key:
            raise ValueError("Missing Supabase credentials. Please check SUPABASE_URL and SUPABASE_KEY in .env")
            
        try:
            self.supabase: Client = create_client(self.supabase_url, self.supabase_key)
            logging.info("Successfully connected to Supabase")
        except Exception as e:
            logging.error(f"Failed to connect to Supabase: {str(e)}")
            raise
    
    def _convert_form_data(self, form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert form data to Supabase format"""
        try:
            # Extract medical assistant data
            medical_data = form_data.get('medical_assistant_data', {})
            
            # Handle injection and exercise therapy values safely
            injection = form_data.get('injection', '')
            exercise_therapy = form_data.get('exercise_therapy', '')
            
            # Generate a timestamp for unique identifiers
            current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            # Ensure we have a valid patient name
            patient_name = form_data.get('patient_name')
            if not patient_name:
                patient_name = f"Patient_{current_time}"
            
            return {
                # Patient Details (required fields)
                "patient_name": patient_name,
                "date_of_birth": form_data.get('dob'),
                "assessment_date": form_data.get('date', datetime.now().strftime('%m/%d/%Y')),
                
                # Treatment Details
                "injection_received": injection.lower() == 'yes' if injection else False,
                "exercise_therapy": exercise_therapy.lower() == 'yes' if exercise_therapy else False,
                
                # Structured Data
                "difficulty_ratings": form_data.get('difficulty_ratings', {}),
                
                # Patient Changes
                "changes_since_last": (
                    form_data.get('patient_changes', {}).get('since_last_treatment', 'Not specified')
                ),
                "changes_since_start": (
                    form_data.get('patient_changes', {}).get('since_start_of_treatment', 'Not specified')
                ),
                "last_three_days": (
                    form_data.get('patient_changes', {}).get('last_3_days', 'Not specified')
                ),
                
                # Pain Symptoms
                "pain_symptoms": form_data.get('pain_symptoms', {}),
                
                # Medical Assistant Data
                "medical_data": medical_data if medical_data else {},
                
                # Raw OCR Data
                "raw_ocr_data": form_data.get('raw_ocr_data', ''),
                
                # Add created_at timestamp
                "created_at": datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            logging.error(f"Error converting form data: {str(e)}")
            logging.error(f"Form data received: {form_data}")
            raise ValueError(f"Error converting form data: {str(e)}")
    
    def store_form_data(self, form_data: Dict[str, Any]) -> Optional[str]:
        """Store form data in Supabase"""
        try:
            # Convert the data
            data = self._convert_form_data(form_data)
            
            # Insert into Supabase
            result = self.supabase.table('patient_assessments')\
                .insert(data)\
                .execute()
            
            # Log success and return the ID
            if result.data:
                assessment_id = result.data[0].get('id')
                logging.info(f"Successfully stored assessment with ID: {assessment_id}")
                return assessment_id
            else:
                raise ValueError("No data returned from insert operation")
                
        except Exception as e:
            logging.error(f"Error storing form data: {str(e)}")
            raise
    
    def get_patient_assessments(self, patient_name: str) -> List[Dict[str, Any]]:
        """Retrieve all assessments for a patient"""
        try:
            result = self.supabase.table('patient_assessments')\
                .select("*")\
                .eq('patient_name', patient_name)\
                .order('assessment_date', desc=True)\
                .execute()
                
            return result.data if result.data else []
            
        except Exception as e:
            logging.error(f"Error retrieving assessments: {str(e)}")
            raise
    
    def get_assessment_by_id(self, assessment_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a specific assessment by ID"""
        try:
            result = self.supabase.table('patient_assessments')\
                .select("*")\
                .eq('id', assessment_id)\
                .limit(1)\
                .execute()
                
            return result.data[0] if result.data else None
            
        except Exception as e:
            logging.error(f"Error retrieving assessment: {str(e)}")
            raise 