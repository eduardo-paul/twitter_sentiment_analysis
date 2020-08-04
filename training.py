#%%
from re import compile
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
tweets = data['tweet'].str.lower()

# %% [markdown]
## Dealing with emails.
# It's extremely hard to write a regexp to catch every possible email, but this simple model should probably work on most relevant instances.

#%%
email_regexp = compile(r'[^\s]+@[^\s]+\.[^\s]+(?:\.[^\s]+)*')
print(f'number of emails in the data set: {tweets.str.contains(email_regexp).sum()}')
tweets = tweets.str.replace(email_regexp, 'EMAIL')

#%% [markdown]
## Dealing with user handles.
# By twitter's rules, user handles have to begin with an '@' followed by letters, numbers and underscores.

#%%
user_handle_regexp = compile(r'@\w+')
print(f'number of user handles in the data set: {tweets.str.contains(user_handle_regexp).sum()}')
tweets = tweets.str.replace(user_handle_regexp, 'USER_HANDLE')

# %% [markdown]
## Dealing with URLs.
# Many times users include URLs in their tweets. They may come in several forms, many time including 'http', 'www', '.com', or the like.

#%%
url_regexp = compile(r'(http[^\s]+|www\.[\w/\.-]+|\w+\.(?:com|org|net))')
print(f'number of urls in the data set: {tweets.str.contains(url_regexp).sum()}')
tweets = tweets.str.replace(url_regexp, 'URL')

# %% [markdown]
## Dealing with repeated letters.
# If a letter appears more than two times in a row, the sequence is replaced with only two repetitions

#%%
repeated_letters_regexp = compile(r'(\w*([a-zA-Z])\2{2,}\w*)')
repeat = tweets.str.extractall(repeated_letters_regexp)
repeat

#%%
repeat.sample(n=100).values