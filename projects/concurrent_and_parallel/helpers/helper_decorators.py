"""
A module containing helper decorators for measuring execution time of functions.
"""
from time import perf_counter


def measure_and_print_time_decorator(function):
    """
    A decorator that measures and prints the execution time of the decorated function.
    :param function: The function to be decorated.
    :return: The wrapper function that measures execution time.
    """
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        result = function(*args, **kwargs)  # the function

        end_time = perf_counter()

        elapsed_time = end_time - start_time
        print(f"{function.__name__}: {elapsed_time:.6f} seconds")
        return result
    return wrapper