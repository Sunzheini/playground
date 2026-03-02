import cProfile


def sample_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


# ------------------------- profile a function -----------------------------------------
cProfile.run('sample_function()', 'profiling/output.prof')


