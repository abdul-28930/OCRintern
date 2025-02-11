from sqlalchemy import create_engine, Column, Integer, String, Date, Float, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()

class PatientAssessment(Base):
    __tablename__ = 'patient_assessments'
    
    id = Column(Integer, primary_key=True)
    assessment_date = Column(Date, nullable=False, default=date.today)
    
    # Patient Details
    patient_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date)
    
    # Treatment Details
    injection_received = Column(Boolean)
    exercise_therapy = Column(Boolean)
    
    # Difficulty Ratings (0-5)
    difficulty_ratings = Column(JSON)  # Stores bending, shoes, sleeping
    
    # Patient Changes
    changes_since_last = Column(String(500))
    changes_since_start = Column(String(500))
    last_three_days = Column(String(50))
    
    # Pain Symptoms (0-10)
    pain_symptoms = Column(JSON)  # Stores pain, numbness, tingling, etc.
    
    # Medical Assistant Inputs
    blood_pressure = Column(String(20))
    heart_rate = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    spo2 = Column(Float)
    temperature = Column(Float)
    blood_glucose = Column(Float)
    respirations = Column(Integer)
    
    # Raw OCR Data
    raw_ocr_data = Column(JSON) 