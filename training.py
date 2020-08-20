#%%
from pandas import read_csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

### DATA INGESTION

data = read_csv(
    'data/train.csv',
    names=['sentiment', 'id', 'date', 'query', 'handle', 'tweet']
)

X = data['tweet']
# 0->negative, 1->positive
y = data['sentiment'].replace(to_replace=4, value=1)

### PIPELINE CREATION 

pipe = make_pipeline(
    # pre-processing
    CountVectorizer(),
    # training
    MultinomialNB()
)

### CROSS-VALIDATION DEFINITION

k_fold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=101
)

### TRAINING AND VALIDATION

scores = cross_val_score(
    pipe,
    X,
    y,
    cv=k_fold,
    n_jobs=-1
)

with open('score.txt', 'w') as file:
    file.write(
        f'mean score: {scores.mean()}\nstd dev: {scores.std()}\n'
    )

#%%
