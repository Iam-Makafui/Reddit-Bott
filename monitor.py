import time
from reddit_client import get_reddit_client
from analyzer import analyze_text
from supabase_client import save_analysis
from config import SUBREDDIT

def monitor_comments():
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(SUBREDDIT)

    for comment in subreddit.stream.comments(skip_existing=True):
        analyzed_text = analyze_text(comment.body)
        save_analysis(comment.body, analyzed_text)
        print(f"Processed: {comment.body}\nSaved: {analyzed_text}")

if __name__ == "__main__":
    while True:
        try:
            monitor_comments()
        except Exception as e:
            print("Error:", e)
        time.sleep(10)  # Wait before retrying
