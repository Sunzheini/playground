import cProfile
import pstats

from memory_profiler import profile


def sample_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


# ------------------------- profile a function -----------------------------------------
# cProfile.run('sample_function()', 'profiling/output.prof')
#
# # Read and sort the stats
# p = pstats.Stats('profiling/output.prof')
# p.strip_dirs().sort_stats('cumulative').print_stats(20)  # Top 20 by cumulative time
# p.sort_stats('time').print_stats(20)  # Top 20 by internal time
# p.sort_stats('calls').print_stats(20)  # Top 20 by number of calls


# ------------------------- memory profiling (requires memory_profiler package) --------
@profile
def memory_intensive():
    large_list = [i**2 for i in range(100000)]
    large_dict = {i: i**2 for i in range(50000)}
    return len(large_list) + len(large_dict)


memory_intensive()
