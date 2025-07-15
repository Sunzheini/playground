# ------------------------------------------------------------------
## Recursion: a function that calls itself
# ------------------------------------------------------------------

# factorial definition is x!= x * (x-1) * (x-2) * (x-3) ... 1.
def factorial(n: int) -> int:
    """Returns the factorial of n."""
    if n == 0 or n == 1:            # Base case for recursion (дъно)
        return 1

    return n * factorial(n - 1)     # Recursive case


# Fibonacci sequence: a sequence where each number is the sum of the
# two preceding ones, usually starting with 0 and 1.
# F(n) = F(n-1) + F(n-2), where F(n) represents the nth Fibonacci number.


def array_sum_calculation(my_list):
    """Returns the sum of all elements in the list."""
    if not my_list:                 # Base case: if the list is empty
        return 0

    return my_list[0] + array_sum_calculation(my_list[1:])


print(array_sum_calculation([5, 4, 3, 2, 3]))



