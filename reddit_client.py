import praw
from config import REDDIT_CONFIG

def get_reddit_client():
    return praw.Reddit(
        client_id=REDDIT_CONFIG["client_id"],
        client_secret=REDDIT_CONFIG["client_secret"],
        user_agent=REDDIT_CONFIG["user_agent"],
        username=REDDIT_CONFIG["username"],
        password=REDDIT_CONFIG["password"]
    )
