import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

REDDIT_CONFIG = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": os.getenv("REDDIT_USER_AGENT"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
}

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

TOGETHER_AI_KEY = os.getenv("TOGETHER_AI_KEY")
TOGETHER_AI_MODEL = os.getenv("TOGETHER_AI_MODEL")

SUBREDDIT = os.getenv("SUBREDDIT")