import pickle
from random import shuffle
from re import compile
from pandas import read_csv
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.classify import accuracy

### Data ingestion

data = read_csv(
    'data/train.csv',
    names=['sentiment', 'id', 'date', 'query', 'handle', 'tweet']
)[:10000] ####### FOR TESTING PURPOSES!!!

sentiments = data['sentiment']
sentiments = sentiments.replace(to_replace=4, value=1) # 0->negative, 1->positive
tweets = data['tweet'].str.lower()

### Data processing

## Dealing with emails.
# It's extremely hard to write a regexp to catch every possible email, but this simple model should probably work on most relevant instances.

email_regexp = compile(r'[^\s]+@[^\s]+\.[^\s]+(?:\.[^\s]+)*')
print(f'number of emails in the data set: {tweets.str.contains(email_regexp).sum()}')
tweets = tweets.str.replace(email_regexp, 'EMAIL')

## Dealing with user handles.
# By twitter's rules, user handles have to begin with an '@' followed by letters, numbers and underscores.

user_handle_regexp = compile(r'@\w+')
print(f'number of user handles in the data set: {tweets.str.contains(user_handle_regexp).sum()}')
tweets = tweets.str.replace(user_handle_regexp, 'USER_HANDLE')

## Dealing with URLs.
# Many times users include URLs in their tweets. They may come in several forms, many time including 'http', 'www', '.com', or the like.

url_regexp = compile(r'(http[^\s]+|www\.[\w/\.-]+|\w+\.(?:com|org|net))')
print(f'number of urls in the data set: {tweets.str.contains(url_regexp).sum()}')
tweets = tweets.str.replace(url_regexp, 'URL')

## Dealing with repeated letters.
# If a letter appears more than two times in a row, the sequence is replaced with only two repetitions

repeated_letters_regexp = compile(r'([a-zA-Z])\1{2,}')
tweets = tweets.str.replace(
    repeated_letters_regexp,
    lambda m: 2*m.group(1)
)
# This data set presents some uncompiled html code. Here we are replacing the &quot; sequence by " so we can we rid of it when tokenizing.
tweets = tweets.str.replace('&quot;', '"')

tweets = tweets.apply(word_tokenize)

### Training.
all_words = FreqDist(
    word.lower()
    for tweet in tweets
    for word in tweet
)

NUM_OF_FEATURES = 2000
word_features = list(all_words)[:NUM_OF_FEATURES]

def tweet_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features[f'contains({word})'] = (word in tweet_words)
    return features

featureset = [
    (tweet_features(tweet), sentiment)
    for tweet, sentiment in zip(tweets, sentiments)
]

shuffle(featureset)

TRAIN_SET_FRAC = 0.8
train_set_len = round(len(featureset) * TRAIN_SET_FRAC)
test_set_len = len(featureset) - train_set_len

train_set = featureset[:train_set_len]
test_set = featureset[train_set_len:]

classifier = NaiveBayesClassifier.train(train_set)

with open('trained_classifier.pkl', 'wb') as file:
    pickle.dump(classifier, file)

print(accuracy(classifier, test_set))
