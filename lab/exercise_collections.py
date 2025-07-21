from collections import Counter, defaultdict, namedtuple, deque
"""
The collections module provides specialized container datatypes that extend 
Python's built-in containers (list, dict, tuple). These are optimized for 
specific use cases and offer enhanced functionality.
"""

# Grouping items by category
inventory = defaultdict(list)  # Defaults to empty list
items = [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana')]

for category, item in items:
    inventory[category].append(item)

print(inventory)
# defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']})


# Count word frequencies
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)

print(word_counts.most_common(2))  # [('apple', 3), ('banana', 2)]
print(word_counts['apple'])  # 3
print(word_counts['pear'])  # 0 (no KeyError)


# Define a Point type
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)

print(p.x, p.y)  # 11 22 (more readable than p[0], p[1])
print(p._asdict())  # {'x': 11, 'y': 22}
