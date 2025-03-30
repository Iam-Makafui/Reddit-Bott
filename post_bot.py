# import praw
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# def post_to_subreddit(subreddit, title, url, flair_text):
#     # Fetch available flairs
#     flair_options = {flair['text']: flair['id'] for flair in subreddit.flair.link_templates}

#     # Ensure the flair is valid
#     if flair_text and flair_text not in flair_options:
#         print(f"⚠️ Invalid flair. Available flairs: {list(flair_options.keys())}")
#         return

#     # Submit the post with the selected flair ID
#     post = subreddit.submit(title, url=url, flair_id=flair_options[flair_text] if flair_text else None)

#     print(f"✅ Post submitted successfully: {post.url}")

# # Initialize Reddit with credentials from .env
# reddit = praw.Reddit(
#     client_id=os.getenv("REDDIT_CLIENT_ID"),
#     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
#     user_agent=os.getenv("REDDIT_USER_AGENT"),
#     username=os.getenv("REDDIT_USERNAME"),
#     password=os.getenv("REDDIT_PASSWORD")
# )

# # Check if authentication is successful
# try:
#     print(f"Authenticated as: {reddit.user.me()}")
# except Exception as e:
#     print(f"Authentication failed: {e}")
#     exit()  # Stop script if login fails

# subreddit_name = input("Enter subreddit name: ").strip()
# subreddit = reddit.subreddit(subreddit_name)

# title = input("Enter post title: ").strip()
# url = input("Enter post URL (required for r/technology): ").strip()

# # Show available flairs before asking for input
# print("Fetching available flairs...")
# flair_options = {flair['text']: flair['id'] for flair in subreddit.flair.link_templates}
# if flair_options:
#     print("Available flairs:", list(flair_options.keys()))

# flair_text = input("Enter post flair (leave blank for none): ").strip()

# post_to_subreddit(subreddit, title, url, flair_text)
import praw
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def post_to_subreddit(subreddit, title, url, flair_text):
    # Fetch available flairs
    flair_options = {flair['text']: flair['id'] for flair in subreddit.flair.link_templates}

    # Ensure the flair is valid
    if flair_text and flair_text not in flair_options:
        print(f"⚠️ Invalid flair. Available flairs: {list(flair_options.keys())}")
        return

    # Submit the post with the selected flair ID
    post = subreddit.submit(title, url=url, flair_id=flair_options[flair_text] if flair_text else None)

    # Print the actual Reddit post URL
    print(f"✅ Post submitted successfully: https://www.reddit.com{post.permalink}")

# Initialize Reddit with credentials from .env
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

# Check if authentication is successful
try:
    print(f"Authenticated as: {reddit.user.me()}")
except Exception as e:
    print(f"Authentication failed: {e}")
    exit()  # Stop script if login fails

subreddit_name = input("Enter subreddit name: ").strip()
subreddit = reddit.subreddit(subreddit_name)

title = input("Enter post title: ").strip()
url = input("Enter post URL (required for r/technology): ").strip()

# Show available flairs before asking for input
print("Fetching available flairs...")
flair_options = {flair['text']: flair['id'] for flair in subreddit.flair.link_templates}
if flair_options:
    print("Available flairs:", list(flair_options.keys()))

flair_text = input("Enter post flair (leave blank for none): ").strip()

post_to_subreddit(subreddit, title, url, flair_text)
