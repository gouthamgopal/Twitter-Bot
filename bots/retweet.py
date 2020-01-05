# This bot is used for retweeting tweets that match a certain keyword using twweepy.

import tweepy
import logging
from config import create_api
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id: {tweet.id}")
        # Not to do anything if that tweet is a reply or its my own tweet.
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return

        if not tweet.favorited:
            try:
                tweet.favorite()
            except:
                logger.error("Error on like", exc_info=True)
        
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except:
                logger.error("Error on retweeting", exc_info=True)
    
    def on_error(self, status):
        logger.error(status)

def helper(keywords):
    api = create_api()
    tweets_listener = TweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    helper(["Python", "Tweepy"])