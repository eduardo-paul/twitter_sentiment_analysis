#%%
from pathlib import Path
from numpy import linspace
from pandas import read_csv
from scipy.stats import norm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import RandomizedSearchCV
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

pipe = make_pipeline(
    # pre-processing
    pt.CountVectorizer(
        ngram_range=(1, 2),
    ),
    TfidfTransformer(),
    # training
    LinearSVC(),
)

### CROSS-VALIDATION DEFINITION

k_fold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=101
)

### TRAINING AND VALIDATION

#scores = cross_val_score(
#    pipe,
#    X,
#    y,
#    cv=k_fold,
#    n_jobs=-1
#)

### GRID SEARCHING

parameters = {'linearsvc__C': norm(loc=.23, scale=.1)}

grid_search = RandomizedSearchCV(
    estimator=pipe,
    param_distributions=parameters,
    n_iter=10,
    cv = k_fold,
    n_jobs=-1,
)

grid_search.fit(X, y)

results = grid_search.cv_results_

lt.log_grid_search(
    pipe,
    results,
    Path('./grid_search_results.txt'),
)
