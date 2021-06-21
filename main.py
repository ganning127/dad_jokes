#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import sys
import os
import requests
import tweepy

def twitterCredentialsSetup():
    '''
    Function gets login credentials for account from twitter_credentials.text
    '''

    with open("twitter_credentials.txt", 'r') as file:
        contents = file.readlines()
        for i in  range(len(contents)):
            contents[i] = contents[i].strip("\n")

    return contents[0], contents[1], contents[2], contents[3]

class DadJokeMaker:
    def __init__(self):
        self.URL = "https://icanhazdadjoke.com/"

    def getDadJoke(self):
        '''
        Function returns a dad joke using the icanhazdadjoke API
        '''
        headers = {'Accept': 'application/json'}
        response = requests.get(self.URL, headers=headers).json()
        return response["joke"]

class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(TWITTER_API_CONSUMER_KEY, TWITTER_API_CONSUMER_SECRET)
        self.auth.set_access_token(TWITTER_API_TOKEN, TWITTER_API_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)
        self.tweets = 0

    def tweet(self, message):
        '''
        Function gets the tweet number and tweets it on Twitter
        '''
        with open("tweet_tracker.txt", "r+") as file:
            tweet_number = int(file.read()) + 1
            self.tweets = tweet_number
            file.truncate(0)
            file.seek(0)
            file.write(str(tweet_number))

        tweet_message = "#" + str(tweet_number) + ": " + message
        self.api.update_status(tweet_message)

    def update_profile(self):
        description = f'High quality dad jokes made purely for laughs.\nJoke Count: {self.tweets}'
        self.api.update_profile(description=description)

TWITTER_API_CONSUMER_KEY, TWITTER_API_CONSUMER_SECRET, TWITTER_API_TOKEN, TWITTER_API_TOKEN_SECRET = twitterCredentialsSetup()

dad = DadJokeMaker()
twitter = Twitter()

joke = dad.getDadJoke()
twitter.tweet(joke)
twitter.update_profile()
