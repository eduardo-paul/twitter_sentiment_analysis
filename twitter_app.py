from requests import get
from requests_oauthlib import OAuth1
from json import loads

search_term = 'twitter'
twitter_request = f'https://stream.twitter.com/1.1/statuses/filter.json?track={search_term}'

with open('credentials.json', 'r') as credentials:
    creds = loads(
                credentials.read()
            )

response = get(
    twitter_request,
    auth = OAuth1(*creds.values()),
    stream = True
)
