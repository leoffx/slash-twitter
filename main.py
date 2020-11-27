import twitterClient
import redditClient
import os

twitter_client = twitterClient.twitterClient()
reddit_client = redditClient.redditClient()

if __name__ == '__main__':
    titles_list = twitter_client.get_last_tweets_ids()
    post_list = reddit_client.get_hot_posts(limit=13, upvote_threshold=15)
    for post in post_list:
        post_title = post['title']
        if post_title[:20] not in titles_list:
            message = f"{post_title}\nreddit.com/{post['id']}\n#{os.getenv('REDDIT_SUBREDDIT')}"
            finished = twitter_client.tweet(message, post['url'])
            if finished:
                print(f"Posted {post['id']}.")
                break
    else:
        print('No new posts found.')
