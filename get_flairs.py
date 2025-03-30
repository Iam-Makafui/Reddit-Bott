from reddit_client import get_reddit_client

def get_subreddit_flairs(subreddit_name):
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    print(f"Available flairs for r/{subreddit_name}:")
    for template in subreddit.flair.link_templates:
        print(f"ID: {template['id']}, Text: {template['text']}")

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    get_subreddit_flairs(subreddit)

