from database.db_handler import DatabaseHandler
import logging
import os
from dotenv import load_dotenv, find_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_database():
    try:
        # Find and load .env file
        env_path = find_dotenv()
        if env_path:
            print(f"✓ Found .env file at: {env_path}")
            load_dotenv(env_path)
        else:
            print("✗ Could not find .env file")
            return

        # Print environment variables (without sensitive data)
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        print(f"\nSupabase URL exists: {bool(supabase_url)}")
        print(f"Supabase Key exists: {bool(supabase_key)}")
        
        # Initialize database handler
        db = DatabaseHandler()
        print("\n✓ Successfully connected to Supabase!")
        
        # Try a simple query - fixed syntax
        result = db.supabase.table('patient_assessments').select("*", count='exact').execute()
        count = result.count
        print(f"✓ Database query successful! Found {count} records.")
        
        # Test table structure
        print("\nTable structure:")
        columns = db.supabase.table('patient_assessments').select("*").limit(1).execute()
        if columns.data:
            print("✓ Table exists and has the correct structure")
        else:
            print("✓ Table exists but is empty")
        
    except Exception as e:
        print(f"\n✗ Database test failed: {str(e)}")
        print("\nPlease check:")
        print("1. Your Supabase URL and key in .env")
        print("2. Internet connection")
        print("3. Supabase service status")
        print(f"\nError details: {str(e)}")

if __name__ == "__main__":
    print(f"Current working directory: {os.getcwd()}")
    test_database() 