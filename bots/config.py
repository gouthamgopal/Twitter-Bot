import tweepy
import logging
import os
from auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

logger = logging.getLogger()

"""
To run the config file succesfully you need to generate the below 4 keys from the twitter developer account for the app.
Just reuse the variables, or replace them with the key generated for succesful authentication and use of twitter api.
"""

def create_api():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api