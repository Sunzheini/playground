from functools import partial, lru_cache, reduce
"""
The functools module provides tools for working with functions and other callable 
objects, enabling functional programming patterns and function manipulation.
"""

# Base function
def power(base, exponent):
    return base ** exponent

# Create specialized functions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(3))    # 27


@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call computes, subsequent calls use cache
print(fibonacci(50))  # 12586269025 (instant with cache, very slow without)


# Functional alternative to sum()
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Factorial implementation
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n+1))
print(factorial(5))  # 120
