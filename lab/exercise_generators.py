# ---------------------------------------------------------------------------------------
# Generator vs Iterator
# ---------------------------------------------------------------------------------------
print("=== Generator vs Iterator ===")


# ITERATOR CLASS APPROACH
class SquareIterator:
    """Custom iterator class - verbose"""

    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


# GENERATOR FUNCTION APPROACH
def square_generator(n):
    """Generator function - simpler syntax"""
    current = 0
    while current < n:
        yield current ** 2  # yield instead of return
        current += 1


print("\nIterator approach:")
iterator = SquareIterator(5)
for num in iterator:
    print(f"Square: {num}")

print("\nGenerator approach:")
generator = square_generator(5)
for num in generator:
    print(f"Square: {num}")

# Both output: 0, 1, 4, 9, 16


# ---------------------------------------------------------------------------------------
# Basic Generator Function
# ---------------------------------------------------------------------------------------
print("\n=== Basic Generator Functions ===")

def count_up_to(max_value):
    """Simple generator that counts up to max_value"""
    count = 1
    while count <= max_value:
        yield count  # Pauses here, returns control to caller
        count += 1
    # Implicitly returns (raises StopIteration)

# Using the generator
print("Counting up to 5:")
counter = count_up_to(5)

print("First value:", next(counter))  # 1
print("Second value:", next(counter))  # 2
print("Third value:", next(counter))  # 3

# Continue with for loop
print("\nRemaining values:")
for num in counter:  # Continues from where it left off!
    print(num)  # 4, then 5

# Generator is now exhausted
print("\nTrying to get more values:")
try:
    print(next(counter))
except StopIteration:
    print("Generator is exhausted!")


# ---------------------------------------------------------------------------------------
# Generator Expressions
# ---------------------------------------------------------------------------------------
print("\n=== Generator Expressions ===")

# LIST COMPREHENSION (eager - creates full list in memory)
squares_list = [x**2 for x in range(5)]
print(f"List comprehension (eager): {squares_list}")
print(f"Type: {type(squares_list)}")
print(f"Memory: {squares_list.__sizeof__()} bytes")

# GENERATOR EXPRESSION (lazy - creates values on demand)
squares_gen = (x**2 for x in range(5))  # Note: parentheses instead of brackets
print(f"\nGenerator expression (lazy): {squares_gen}")
print(f"Type: {type(squares_gen)}")
print(f"Memory: {squares_gen.__sizeof__()} bytes")

# Consume the generator
print("\nConsuming generator:")
for square in squares_gen:
    print(f"Square: {square}")

# Generator is exhausted after iteration
print("\nAfter consumption:", list(squares_gen))  # Empty list


# ---------------------------------------------------------------------------------------
# Stateful Generators
# ---------------------------------------------------------------------------------------
print("\n=== Stateful Generators ===")


def running_average():
    """Generator that maintains state between calls"""
    total = 0
    count = 0

    while True:
        value = yield  # Pauses to receive a value
        if value is None:
            break  # Exit condition

        total += value
        count += 1
        average = total / count
        yield average  # Yield the result


print("Running average calculator:")
avg_gen = running_average()

# Initialize generator
next(avg_gen)  # Prime the generator (move to first yield)

# Send values and get averages
numbers = [10, 20, 30, 40]

for num in numbers:
    # Send value and get average
    result = avg_gen.send(num)
    print(f"After adding {num}: average = {result}")
    next(avg_gen)  # Move to receive position again

# Close the generator
avg_gen.close()
print("Generator closed")


# ---------------------------------------------------------------------------------------
# Pipeline Pattern with Generators
# ---------------------------------------------------------------------------------------
print("\n=== Generator Pipeline Pattern ===")

def read_lines(file_path):
    """Generator 1: Read lines from file"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def filter_lines(lines, keyword):
    """Generator 2: Filter lines containing keyword"""
    for line in lines:
        if keyword.lower() in line.lower():
            yield line

def process_lines(lines):
    """Generator 3: Process lines (uppercase them)"""
    for line in lines:
        yield line.upper()

# Create a mock file for demonstration
mock_data = [
    "Python generators are powerful",
    "Iterators are also useful",
    "Generator pipelines process data efficiently",
    "Python is great for data processing"
]

# Save mock data to file
with open('sample.txt', 'w') as f:
    f.write('\n'.join(mock_data))

print("Creating generator pipeline:")
# Chain generators together (lazy evaluation!)
pipeline = process_lines(
    filter_lines(
        read_lines('sample.txt'),
        'python'
    )
)

print("\nResults from pipeline:")
for result in pipeline:
    print(f"- {result}")

# Output:
# - PYTHON GENERATORS ARE POWERFUL
# - PYTHON IS GREAT FOR DATA PROCESSING


# ----------------------------------------------------------------------------------------
# Fibonacci Generator Example (Infinite generators)
# ----------------------------------------------------------------------------------------
print("\n=== Infinite Generators ===")

def fibonacci():
    """Infinite Fibonacci sequence generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers:")
fib_gen = fibonacci()

# Use itertools.islice to limit infinite generator
from itertools import islice

first_10 = list(islice(fib_gen, 10))
print(first_10)

# Generator is still alive! Get 5 more
print("\nNext 5 Fibonacci numbers:")
next_5 = list(islice(fib_gen, 5))
print(next_5)

# Practical example: Generate unique IDs
def id_generator(prefix="ID"):
    """Infinite ID generator"""
    counter = 1
    while True:
        yield f"{prefix}_{counter:06d}"
        counter += 1

print("\nUnique ID generator:")
id_gen = id_generator("USER")
for _ in range(5):
    print(next(id_gen))
# Output: USER_000001, USER_000002, etc.
