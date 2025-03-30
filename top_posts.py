from reddit_client import get_reddit_client

def get_top_posts(subreddit_name):
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    posts = []
    for post in subreddit.hot(limit=5):
        posts.append((post.title, post.score, post.url))

    return posts

def display_top_posts():
    city1 = input("Enter the first city subreddit: ")
    city2 = input("Enter the second city subreddit: ")

    print(f"\nTop posts from r/{city1}:")
    for idx, (title, score, url) in enumerate(get_top_posts(city1), 1):
        print(f"{idx}. {title} (Score: {score}) - {url}")

    print(f"\nTop posts from r/{city2}:")
    for idx, (title, score, url) in enumerate(get_top_posts(city2), 1):
        print(f"{idx}. {title} (Score: {score}) - {url}")

if __name__ == "__main__":
    display_top_posts()
