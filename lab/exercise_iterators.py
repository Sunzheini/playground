# ---------------------------------------------------------------------------------------
# Simple example
# ---------------------------------------------------------------------------------------
# Creating a simple iterator from a list
my_list = [1, 2, 3, 4, 5]

# Get an iterator object
my_iterator = iter(my_list)  # or my_list.__iter__()

print("Basic iterator example:")
print("First call to next():", next(my_iterator))  # 1
print("Second call to next():", next(my_iterator))  # 2
print("Third call to next():", next(my_iterator))  # 3
print("Fourth call to next():", next(my_iterator))  # 4
print("Fifth call to next():", next(my_iterator))  # 5

# This will raise StopIteration error - no more items
# print("Sixth call:", next(my_iterator))  # Error!


# ---------------------------------------------------------------------------------------
# Iterator class
# ---------------------------------------------------------------------------------------
class CountDown:
    """Custom iterator that counts down from start to 0"""

    def __init__(self, start):
        self.current = start
        self.start = start

    def __iter__(self):
        """Must return the iterator object itself"""
        return self

    def __next__(self):
        """Must return the next value or raise StopIteration"""
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value


# Using the custom iterator
print("\nCustom CountDown iterator:")
countdown = CountDown(5)

# Method 1: Using next() manually
print("Manual iteration:")
print(next(countdown))  # 5
print(next(countdown))  # 4
print(next(countdown))  # 3

# Method 2: Using for loop (automatically handles StopIteration)
print("\nFor loop iteration:")
for number in CountDown(3):  # Creates new iterator
    print(f"Counting down: {number}")
# Output: 3, 2, 1, 0


# ---------------------------------------------------------------------------------------
# Fibonacci iterator
# ---------------------------------------------------------------------------------------
class Fibonacci:
    """Iterator that generates Fibonacci numbers"""

    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1  # First two Fibonacci numbers

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration

        self.count += 1
        fib_number = self.a
        self.a, self.b = self.b, self.a + self.b  # Calculate next numbers
        return fib_number


print("\nFibonacci iterator:")
fib = Fibonacci(8)  # Generate first 8 Fibonacci numbers

# Convert iterator to list to see all values
fib_numbers = list(fib)
print(f"First 8 Fibonacci numbers: {fib_numbers}")
# Output: [0, 1, 1, 2, 3, 5, 8, 13]


# ---------------------------------------------------------------------------------------
# Iterator vs Iterable
# ---------------------------------------------------------------------------------------
print("\nIterator vs Iterable demonstration:")

# ITERABLE: Can create an iterator (has __iter__ method)
my_list = [1, 2, 3]  # List is iterable
my_string = "abc"    # String is iterable
my_dict = {"a": 1}   # Dict is iterable

# ITERATOR: Has both __iter__ and __next__ methods
list_iterator = iter(my_list)

# Every iterator is also iterable (can be used in for loops)
print("Is list iterable?", hasattr(my_list, '__iter__'))  # True
print("Is iterator iterable?", hasattr(list_iterator, '__iter__'))  # True
print("Is list an iterator?", hasattr(my_list, '__next__'))  # False
print("Is iterator an iterator?", hasattr(list_iterator, '__next__'))  # True


# ---------------------------------------------------------------------------------------
# Practical Example: Pagination Iterator
# ---------------------------------------------------------------------------------------
class Paginator:
    """Iterator for handling API pagination"""

    def __init__(self, total_items, items_per_page):
        self.total_items = total_items
        self.items_per_page = items_per_page
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        start_idx = self.current_page * self.items_per_page

        if start_idx >= self.total_items:
            raise StopIteration

        end_idx = min(start_idx + self.items_per_page, self.total_items)
        page_data = f"Page {self.current_page + 1}: Items {start_idx + 1}-{end_idx}"

        self.current_page += 1
        return page_data


print("\nPagination iterator example:")
paginator = Paginator(total_items=25, items_per_page=10)

for page in paginator:
    print(page)
# Output:
# Page 1: Items 1-10
# Page 2: Items 11-20
# Page 3: Items 21-25
