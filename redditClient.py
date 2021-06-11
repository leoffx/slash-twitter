import io
import praw
import os
import requests


class redditClient:
    def __init__(self):
        reddit_key = os.getenv("REDDIT_KEY")
        reddit_secret = os.getenv("REDDIT_SECRET")

        self.reddit = praw.Reddit(client_id=reddit_key,
                                  client_secret=reddit_secret,
                                  user_agent="bonsai bot")

    def get_hot_posts(self, limit=20, upvote_threshold=10):
        """"Get top posts, and post them if they were not posted
        yet, and have more than the set ammount of upvotes."""

        posts = list(self.reddit.subreddit(os.getenv("REDDIT_SUBREDDIT")).hot(limit=limit))

        post_list = []
        for post in posts:
            if post.pinned or post.stickied:
                continue
            photo_list = []
            post_upvotes = post.ups
            try:
                photo_list.append(post.preview['images'][0]['source']['url'])
            except AttributeError:
                try:
                    for a in post.media_metadata.values():
                        photo_list.append(a['s']['u'])
                except AttributeError:
                    continue
            if post_upvotes > upvote_threshold and photo_list:
                post_title = post.title
                post_id = post.id
                post_list.append(
                    {'title': post_title, 'id': post_id, 'url': photo_list})

        return post_list
