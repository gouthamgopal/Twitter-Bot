# Twitter-Bot

> https://twitter.com/TwitBot94189404

This is a twitter bot developed using python and its twitter library Tweepy.

Twitter bots are mainly automated programs which intend on performing a specific task. In this repo,
I have created 3 twitter bots for academic development purposes.
There are namely 2 twitter bots:
1. Follower bot - This bot will check all the people that are following you and will follow them back. The bot refreshes itself every 60 seconds.
2. Retweet bot - This bot will check for tweets with certain specified keywords in them and these tweets will be liked and retweeted by the account/ bot.

For running this twitter bot application, we have to first create a developer account in twitter and create a development app.
Inside this app you can find the required tokens to access the twitter-api for the particular account.
These are necessary for Tweepy to interact with the twitter api.

Various other twiiter bots can also be created following the similar pattern, and referring to Tweepy documentation.

## Running this application

You can clone this repo into your local machine, install the dependencies and just run the bot python application to run the bot.
Please bear in mind that the config.py refers to 4 keys which are twitter tokens for accessing their API. These keys have to be setup by yourself before runnning the bot.

## Creating an image through docker

We can develop the entire project and then produce an image of the project using Docker.
This will help us in building an image by snapshotting the latest version of it, with all the dependencies which we can access from anywhere by instantiating it in a cloud platform such as AWS.

> A Dockerfile is kept in place as an example for creating an image of a retweet bot.

This will generate a docker instance which can be used to run the twitter bot.
This Docker instance can then be converted into an image file inorder to transport the whole application as zip.

## Running AWS instance for twitter bot

We need to create a new AWS profile for this step.
We can create an EC2 compute instance in the AWS account we created and then create an Ubuntu 18.04 instance for our purpose.
After creating the instance we can connect to this instance via ssh as given in the options for AWS connect.
This will help us work on the AWS EC2 instance we created locally.
Here we can upload the created image file to the AWS instance and unzip it.
After this we can run the application and allow it to keep running even when disconnected according to our preferences.
