import io
import tweepy
import os
import requests


class twitterClient:
    def __init__(self):
        twitter_key = os.getenv("TWITTER_KEY")
        twitter_secret = os.getenv("TWITTER_SECRET")
        twitter_token = os.getenv("TWITTER_ACCESS_TOKEN")
        twitter_token_secret = os.getenv("TWITTER_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(twitter_key, twitter_secret)
        auth.set_access_token(
            twitter_token, twitter_token_secret)

        self.api = tweepy.API(auth)

    def tweet(self, message, image_url):
        try:
            images = []
            for url in image_url[:4]: #Upload up to 4 photos
                image_data = requests.get(url).content
                file_object = io.BytesIO(image_data)
                images.append(self.api.media_upload(file=file_object,
                                                    filename='photo.png').media_id_string)
                if len(message) > 253: #Check if message lenght is within Twitter character limit
                    message = f'{message[:240]}...'

            self.api.update_status(message, media_ids=images)
            return True
        except Exception:
            return False

    def get_last_tweets_ids(self):
        ids = self.api.user_timeline(os.getenv("TWITTER_USERNAME"), count=40)

        titles_list = []

        for id in ids:
            tweet_text = id.text
            title = tweet_text.split('\n')[0]
            titles_list.append(title[:20])

        return titles_list
