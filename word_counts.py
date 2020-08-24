def word_counts(count_vect, X_array):
    '''Receive a scikit-learn CountVectorizer object and its corresponding fitted array and return a reverse-count-sorted list of (word, count) tuples.
    
    Parameters:
    count_vect: sklearn.feature_extraction.text.CountVectorizer()
    X_array: sklearn.feature_extraction.text.CountVectorizer.fit()

    Returns:
    word_counts: list of tuples
    '''

    from numpy import asarray

    words = count_vect.get_feature_names()
    counts = asarray(X_array.sum(axis=0)).flatten()
    word_counts = sorted(
        dict(zip(words, counts)).items(),
        key=lambda entry: entry[1],
        reverse=True
    )
    return word_counts
