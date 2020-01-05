import tweepy
import logging
from config import create_api
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def followers(api):
    logger.info("Retreiving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info("Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    while True:
        followers(api)
        logger.info("wating ....")
        time.sleep(60)

if __name__ == "__main__":
    main()