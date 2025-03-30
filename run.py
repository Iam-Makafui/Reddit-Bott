# import threading
# from monitor import monitor_comments
# from top_posts import display_top_posts
# from post_bot import post_to_subreddit
# from comment_bot import comment_on_posts

# def run_all():
#     threading.Thread(target=monitor_comments).start()
    
#     # Get viral posts
#     display_top_posts()

#     # Post to subreddit
#     subreddit = input("Enter subreddit to post to: ")
#     title = input("Enter post title: ")
#     content = input("Enter post content: ")
#     post_to_subreddit(subreddit, title, content)

#     # Comment on posts
#     subreddit = input("Enter subreddit to comment on: ")
#     comment_on_posts(subreddit)

# if __name__ == "__main__":
#     run_all()

import threading
from monitor import monitor_comments
from top_posts import display_top_posts
from post_bot import post_to_subreddit
from comment_bot import comment_on_posts

def run_all():
    # Get viral posts first
    display_top_posts()

    # Post to subreddit
    subreddit = input("Enter subreddit to post to: ")
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    post_to_subreddit(subreddit, title, content)

    # Comment on posts
    subreddit = input("Enter subreddit to comment on: ")
    comment_on_posts(subreddit)

    # Start monitoring after user inputs
    threading.Thread(target=monitor_comments, daemon=True).start()

if __name__ == "__main__":
    run_all()
