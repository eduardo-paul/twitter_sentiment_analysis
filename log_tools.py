from inspect import cleandoc

def log_scores(pipe, scores, path):
    #preprocessing_list = list(
    #    map(
    #        lambda func: func.__name__,
    #        preprocessors
    #    )
    #)

    log = cleandoc(
        f'''
        pipeline: {pipe}
        scores: {scores}
        mean score: {scores.mean()}
        std dev: {scores.std()}
        '''
    ) + '\n' + 50*'-' + '\n'

    with open(path, 'a') as file:
        file.write(log)
        print('Log file saved.')
