import praw
import requests
import os
from supabase import create_client
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Reddit API Setup
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

# Together AI API Setup (Free)
TOGETHER_AI_KEY = os.getenv("TOGETHER_AI_KEY")
TOGETHER_AI_MODEL = os.getenv("TOGETHER_AI_MODEL")

# Supabase Database Setup
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

# Function to analyze text using Together AI API
def analyze_text(text):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {"Authorization": f"Bearer {TOGETHER_AI_KEY}", "Content-Type": "application/json"}
    data = {
        "model": TOGETHER_AI_MODEL,
        "messages": [{"role": "user", "content": text}]
    }

    response = requests.post(url, headers=headers, json=data)

    # print("Hello")
    # print(response.json())  # Print the response for debugging

    if response.status_code == 200:
        json_response = response.json()  # Ensure we parse it correctly
        if "choices" in json_response and json_response["choices"]:
            return json_response["choices"][0]["message"]["content"]
        else:
            return "Analysis failed: Invalid response format"


# Function to store data in Supabase
def save_to_supabase(original, analyzed):
    data = {"original_text": original, "analysis": analyzed}
    response = supabase.table("reddit_analysis").insert(data).execute()
    print("Saved to Supabase:", response)

# Function to monitor subreddit comments
def monitor_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    
    for comment in subreddit.stream.comments(skip_existing=True):
        analyzed_text = analyze_text(comment.body)
        save_to_supabase(comment.body, analyzed_text)
        print(f"Processed: {comment.body}\nSaved: {analyzed_text}")

if __name__ == "__main__":
    SUBREDDIT = os.getenv("SUBREDDIT")
    while True:
        try:
            monitor_comments(SUBREDDIT)
        except Exception as e:
            print("Error:", e)
        time.sleep(10)  # Wait 10 seconds before retrying
