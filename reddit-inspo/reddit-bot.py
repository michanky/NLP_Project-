import praw
import random
import time
import config as cfg

reddit = praw.Reddit(
    client_id=cfg.CLIENT_ID,
    client_secret=cfg.CLIENT_SECRET,
    user_agent=cfg.USER_AGENT,
    username=cfg.USERNAME,
    password=cfg.PASSWORD
)

inspiration_list = ["You can do it!",
                    "Don't give up!", "I believe in you!", 'Jiayou!', 'Just Do it!']

subreddit = reddit.subreddit('articlessgtest')

for post in subreddit.new(limit=None):
    print(post.title)

    for comment in post.comments:
        if hasattr(comment, 'body'):
            comment_lower = comment.body.lower()
            if ' sad' in comment_lower:
                print("------------")
                print(comment.body)
                index = random.randint(0, len(inspiration_list) - 1)
                inspiration_comment = inspiration_list[index]
                comment.reply(inspiration_comment)
                time.sleep(60)
