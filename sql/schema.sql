-- Enable necessary extensions
create extension if not exists "uuid-ossp";

-- Create patient_assessments table
create table patient_assessments (
    id uuid default uuid_generate_v4() primary key,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    
    -- Patient Details
    patient_name text not null,
    date_of_birth date,
    assessment_date date not null,
    
    -- Treatment Details
    injection_received boolean default false,
    exercise_therapy boolean default false,
    
    -- Structured Data
    difficulty_ratings jsonb default '{}'::jsonb,
    changes_since_last text,
    changes_since_start text,
    last_three_days text,
    pain_symptoms jsonb default '{}'::jsonb,
    medical_data jsonb default '{}'::jsonb,
    raw_ocr_data text,
    
    -- Add constraints
    constraint valid_difficulty_ratings check (jsonb_typeof(difficulty_ratings) = 'object'),
    constraint valid_pain_symptoms check (jsonb_typeof(pain_symptoms) = 'object'),
    constraint valid_medical_data check (jsonb_typeof(medical_data) = 'object')
);

-- Create indexes
create index idx_patient_assessments_patient_name 
    on patient_assessments (patient_name);
create index idx_patient_assessments_date 
    on patient_assessments (assessment_date desc);

-- Enable Row Level Security
alter table patient_assessments enable row level security;

-- Create policies
create policy "Enable all operations for authenticated users" 
    on patient_assessments for all using (auth.role() = 'authenticated'); 