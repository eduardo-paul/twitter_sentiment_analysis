from inspect import cleandoc

def log_scores(pipe, scores, path):

    log = cleandoc(
        f'''
        pipeline: {pipe}
        scores: {scores}
        mean score: {scores.mean()}
        std dev: {scores.std()}
        '''
    ) + '\n' + 50*'-' + '\n\n'

    with open(path, 'a') as file:
        file.write(log)
        print('Log file saved.')

def log_grid_search(pipe, results, path):

    log = cleandoc(
        f'''
        pipeline: {pipe}
        results: {results}
        '''
    ) + '\n' + 50*'-' + '\n\n'

    with open(path, 'a') as file:
        file.write(log)
        print('Log file saved.')
