from itertools import count, cycle, repeat, islice, tee, chain, product, permutations, combinations, \
    combinations_with_replacement, groupby, takewhile, filterfalse

"""
The itertools module provides a collection of fast, memory-efficient tools
for working with iterators. It's essential for advanced iteration patterns
and combinatorial operations.
"""

# Generate IDs starting from 1000
for id in count(1000):
    if id > 1005: break
    print(id)  # 1000, 1001, ..., 1005

# Cycle through colors indefinitely
colors = cycle(['red', 'green', 'blue'])
print(next(colors), next(colors))  # red, green

# Repeat a value
squares = map(pow, range(5), repeat(2))  # [0**2, 1**2, 2**2, ...]


# Generate coordinate grid
for x, y in product([0, 1], repeat=2):
    print(f"({x},{y})")  # (0,0), (0,1), (1,0), (1,1)

# Get all 2-letter arrangements of 'ABC'
print(list(permutations('ABC', 2)))  # [('A','B'), ('A','C'), ...]

# Get unique pairs
print(list(combinations('ABC', 2)))  # [('A','B'), ('A','C'), ('B','C')]


# Merge multiple lists
merged = chain([1, 2], ['a', 'b'], range(3))
print(list(merged))  # [1, 2, 'a', 'b', 0, 1, 2]

# Group data by key
data = sorted([('A', 1), ('B', 2), ('A', 3)], key=lambda x: x[0])
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))  # A [('A',1), ('A',3)], B [('B',2)]

# Slice an infinite iterator
first_5_even = islice(count(0, 2), 5)  # 0, 2, 4, 6, 8


# Take numbers while < 5
print(list(takewhile(lambda x: x < 5, [1, 3, 6, 2])))  # [1, 3]

# Get non-alphabetic characters
chars = filterfalse(str.isalpha, 'A1B2C3')
print(''.join(chars))  # '123'