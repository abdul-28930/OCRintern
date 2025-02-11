from supabase import create_client
import os
from dotenv import load_dotenv

def test_supabase_connection():
    # Load environment variables
    load_dotenv()
    
    # Get credentials
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    print("\nChecking Supabase credentials:")
    print(f"URL exists: {bool(url)}")
    print(f"Key exists: {bool(key)}")
    
    if not url or not key:
        print("\n✗ Missing credentials in .env file")
        return
    
    try:
        # Try to connect
        supabase = create_client(url, key)
        
        # Test connection with a simple query
        response = supabase.table('patient_assessments').select("*", count='exact').execute()
        
        print("\n✓ Successfully connected to Supabase!")
        print(f"✓ Found {response.count} records in patient_assessments table")
        
        # Verify table structure
        print("\nVerifying table structure...")
        columns = supabase.table('patient_assessments').select("*").limit(1).execute()
        if columns.data:
            print("✓ Table exists and has data")
            print("\nColumns available:")
            for key in columns.data[0].keys():
                print(f"  - {key}")
        else:
            print("✓ Table exists but is empty")
        
    except Exception as e:
        print(f"\n✗ Connection failed: {str(e)}")

if __name__ == "__main__":
    test_supabase_connection() 