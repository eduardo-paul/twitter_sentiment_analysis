#%%
import pandas as pd

#%%
data = pd.read_csv(
    'data/train.csv',
    names=['sentiment', 'id', 'date', 'query', 'handle', 'tweet']
)

#%%
data.shape

#%%
sentiments = data['sentiment']
tweets = data['tweet']

# %% [markdown]
## Dealing with emails.
# It's extremely hard to write a regexp to catch every possible email, but this simple model should probably work on most relevant instances.

#%%
tweets = tweets.str.replace(r'\w+@\w+\.\w+[\.\w+]', 'EMAIL')]

#%% [markdown]
## Dealing with user handles.
# By twitter's rules, user handles have to begin with an '@' followed by letters, numbers and underscores.
# In this dataset, there are exactly 4 ocurrences of the word USERNAME, so we can use it as a replacement for user handles without needing to worry.

#%%
# Regexp for user handles.
expected_handle = r'(@\w+)'

#%%
tweets[tweets.str.contains('USERNAME')]

#%%
tweets = tweets.str.replace(expected_handle, 'USERNAME')

#%%
tweets[tweets.str.contains('\s@\s')]

# %% [markdown]
## Dealing with URLs.
# Many times users include URLs in their tweets. They may come in several forms, many time including 'http', 'www', '.com', or the like.

#%%
tweets = tweets.str.replace(r'(http[^\s]+)', 'URL')

#%%
tweets = tweets.str.replace(r'www\.[\w/\.-]+', 'URL')

#%%
test = tweets[tweets.str.contains(r'\.com')]

#%%
test.sample(n=10).values