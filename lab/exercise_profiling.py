import cProfile
import pstats


def sample_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


# ------------------------- profile a function -----------------------------------------
cProfile.run('sample_function()', 'profiling/output.prof')

# Read and sort the stats
p = pstats.Stats('profiling/output.prof')
p.strip_dirs().sort_stats('cumulative').print_stats(20)  # Top 20 by cumulative time
p.sort_stats('time').print_stats(20)  # Top 20 by internal time
p.sort_stats('calls').print_stats(20)  # Top 20 by number of calls


# ------------------------- memory profiling (requires memory_profiler package) --------