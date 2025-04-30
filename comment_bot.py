from reddit_client import get_reddit_client
from analyzer import analyze_text

def comment_on_posts(subreddit_name):
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    for post in subreddit.hot(limit=5):
        analysis = analyze_text(post.title)
        post.reply(analysis)
        print(f"Commented on '{post.title}': {analysis}")


if __name__ == "__main__":
    subreddit = input("Enter subreddit to comment on: ")
    comment_on_posts(subreddit)
