from json import load
import tweepy

with open('credentials.json', 'r') as file:
    credentials = load(file)

auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])

api = tweepy.API(auth)

