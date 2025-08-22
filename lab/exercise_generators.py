def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Pauses here, returns count
        count += 1   # Resumes here when next() is called

# Usage:
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5
# print(next(counter))  # Raises StopIteration error when max is exceeded


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2
print(next(fib))  # 3
print(next(fib))  # 5
print(next(fib))  # 8