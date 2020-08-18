#%%
import pickle
from random import shuffle
from pandas import read_csv
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.classify import accuracy

data = read_csv(
    'data/train.csv',
    names=['sentiment', 'id', 'date', 'query', 'handle', 'tweet']
)[:10000] ####### CHANGE THIS!!!!!!

sentiments = data['sentiment']
sentiments = sentiments.replace(to_replace=4, value=1)

tweets = data['tweet']
tweets = tweets.apply(
    lambda tweet: word_tokenize(tweet.lower())
)

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
#%%
