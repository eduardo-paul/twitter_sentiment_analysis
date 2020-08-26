#%%
from pathlib import Path
from pandas import read_csv
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import preproc_tools as pt
import log_tools as lt

### DATA INGESTION

data = read_csv(
    Path('./data/train.csv'),
    names=['sentiment', 'id', 'date', 'query', 'handle', 'tweet']
)

X = data['tweet']
# 0->negative, 1->positive
y = data['sentiment'].replace(to_replace=4, value=1)

### PIPELINE CREATION 

preprocessors = [
    #pt.email_proc,
    #pt.handle_proc,
    #pt.url_proc,
    #pt.mult_letters_proc,
    #pt.html_proc,
]

pipe = make_pipeline(
    # pre-processing
    pt.CustomVectorizer(
        preprocessors=preprocessors,
        ngram_range=(2, 2),
    ),
    # training
    MultinomialNB()
)

### CROSS-VALIDATION DEFINITION

k_fold = KFold(
    n_splits=10,
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

lt.log_scores(pipe, scores, Path('./score.txt'))
