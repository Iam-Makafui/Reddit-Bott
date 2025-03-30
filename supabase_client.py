from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_analysis(original, analyzed):
    data = {"original_text": original, "analysis": analyzed}
    response = supabase.table("reddit_analysis").insert(data).execute()
    print("Saved to Supabase:", response)
