from re import sub

def email_proc(tweet):
    '''Replace every email in the tweet by the string "EMAIL". The regexp used here is simple but should be enough for most cases.'''
    email_regexp = r'[^\s]+@[^\s]+\.[^\s]+(?:\.[^\s]+)*'
    return sub(email_regexp, 'EMAIL', tweet)

def handle_proc(tweet):
    '''Replace user handles by the string "USER_HANDLE".'''
    user_handle_regexp = r'@\w+'
    return sub(user_handle_regexp, 'USER_HANDLE', tweet)

def url_proc(tweet):
    '''Replace urls in various format by the string "URL".'''
    url_regexp = r'(http[^\s]+|www\.[\w/\.-]+|\w+\.(?:com|org|net))'
    return sub(url_regexp, 'URL', tweet)

def mult_letters_proc(tweet):
    '''If a letter appears more than two times in a row, replace it with only two repetitions.'''
    repeated_letters_regexp = r'([a-zA-Z])\1{2,}'
    return sub(
        repeated_letters_regexp,
        lambda m: 2*m.group(1),
        tweet
    )

def html_proc(tweet):
    '''This data set presents some uncompiled html code. Here we are replacing the &quot; sequence by " so we can get rid of it when tokenizing.'''
    return sub('&quot;', '"', tweet)
