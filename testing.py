#%%
from pathlib import Path
from pandas import read_csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

### DATA INGESTION

train_data = read_csv(
    Path('./data/train.csv'),
    names=['sentiment', 'id', 'date', 'query_train', 'handle', 'tweet']
)

X_train = train_data['tweet']
# 0->negative, 1->positive
y_train = train_data['sentiment'].replace(to_replace=4, value=1)

### TRAINING AND TESTING

pipe = make_pipeline(
    # pre-processing
    CountVectorizer(
        ngram_range=(1, 2),
    ),
    TfidfTransformer(),
    # training
    LinearSVC(C=0.29),
)

pipe.fit(X_train, y_train)

test_data = read_csv(
    Path('./data/test.csv'),
    names=['sentiment', 'id', 'date', 'query_train', 'handle', 'tweet']
)

# The test dataset contains neutral tweets. Since the model was trained using only pos/neg sentiments, it would not be fair to include the neutral ones in the test.
test_data = test_data[test_data['sentiment'] != 2]

X_test = test_data['tweet']
y_test = test_data['sentiment'].replace(to_replace=4, value=1)

pipe.score(X_test, y_test)
# Final score of 0.841225626740947
