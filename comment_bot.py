from reddit_client import get_reddit_client
from analyzer import analyze_text

def comment_on_posts(subreddit_name):
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    for post in subreddit.hot(limit=5):
        analysis = analyze_text(post.title)
        comment_text = f"AI Analysis: {analysis}"
        post.reply(comment_text)
        print(f"Commented on '{post.title}': {comment_text}")

if __name__ == "__main__":
    subreddit = input("Enter subreddit to comment on: ")
    comment_on_posts(subreddit)
