from requests import get
from requests_oauthlib import OAuth1
from json import load, loads

SEARCH_TERM = 'brasil'
LANGUAGE = 'pt'
twitter_request = f'https://stream.twitter.com/1.1/statuses/filter.json?track={SEARCH_TERM}&language={LANGUAGE}'

with open('credentials.json', 'r') as file:
    credentials = load(file).values()

response = get(
    twitter_request,
    auth=OAuth1(*credentials),
    stream=True
)

for chunk in response.iter_content(chunk_size=None):
    tweet = loads(chunk)['text']
    print(tweet)
