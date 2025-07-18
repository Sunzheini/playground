# Dynamic programming (Динамично оптимиране)

"""
Dynamic programming is a controlled brute-force algorithm
that solves problems by breaking them down into simpler subproblems
and storing the results of these subproblems to avoid redundant
calculations. It is particularly useful for optimization problems
and can significantly reduce the time complexity compared to naive
recursive approaches.

Memoization is a technique used in dynamic programming
to store the results of expensive function calls and reuse them
when the same inputs occur again, thus avoiding the need for
repeated calculations.

Guessing is a technique used in dynamic programming
to make educated guesses about the optimal solution
to a problem based on previously computed results.
"""

# -------------------------------------------------------------------
# Fibonacci sequence using dynamic programming
def fibonacci_recursive_with_memorization(n, memo=None):
    """Returns the nth Fibonacci number using recursion with memoization."""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n <= 2:
        return 1

    # Store the result in the memo dictionary
    result = fibonacci_recursive_with_memorization(n - 1, memo) + fibonacci_recursive_with_memorization(n - 2, memo)
    memo[n] = result
    return result


def fibonacci_optimal(n):
    """Returns the nth Fibonacci number using dynamic programming."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# -------------------------------------------------------------------
from time import perf_counter

fib_number = 10

start_time = perf_counter()
print(fibonacci_recursive_with_memorization(fib_number, {}))  # Output: 55
end_time = perf_counter()
print(f"{end_time - start_time:.6f} seconds")

start_time = perf_counter()
print(fibonacci_optimal(fib_number))
end_time = perf_counter()
print(f"{end_time - start_time:.6f} seconds")


