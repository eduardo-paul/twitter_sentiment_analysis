from requests import get
from requests_oauthlib import OAuth1
from json import loads

search_term = 'economics'
twitter_request = f'https://stream.twitter.com/1.1/statuses/filter.json?track={search_term}'

with open('credentials.json', 'r') as credentials:
    creds = loads(
        credentials.read()
    ).values()

response = get(
    twitter_request,
    auth = OAuth1(*creds),
    stream=True
)

count = 0
for chunk in response.iter_content(chunk_size=None):
    tweet = loads(chunk)['text']
    print(tweet)
    if count < 10:
        count += 1
    else:
        break
