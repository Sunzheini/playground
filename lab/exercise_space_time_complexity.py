"""
Space and time complexity are fundamental concepts in computer science used to analyze how efficient
an algorithm is. They help you answer the question: "How does this algorithm scale as the
input gets larger?"
"""


# ------------------------------------------------------------------------------------------
# 1. Time Complexity
# ------------------------------------------------------------------------------------------
"""
Time complexity measures how the execution time of an algorithm grows as the input size increases. 
We typically express this using Big O notation, which describes the upper bound of growth.
"""

## Common Time Complexities (Best to Worst)
"""
Notation	Name	        Description	                                            Example
O(1)	    Constant	    Time doesn't depend on input size	                    Accessing array element by index
O(log n)	Logarithmic	    Time grows slowly, doubling input adds constant time	Binary search
O(n)	    Linear	        Time grows proportionally to input	                    Simple loop through array
O(n log n)	Linearithmic	Common in efficient sorting	                            Merge sort, Quick sort (avg)
O(n²)	    Quadratic	    Time grows with square of input	                        Nested loops, Bubble sort
O(2ⁿ)	    Exponential	    Time doubles with each input addition	                Recursive Fibonacci (naive)
O(n!)	    Factorial	    Extremely slow growth	                                Permutations, Traveling salesman (brute force)
"""

## Visual Growth Comparison
"""
Input Size (n)  | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ)
----------------|------|----------|------|------------|-------|-------
n = 10          | 1    | ~3       | 10   | ~33        | 100   | 1,024
n = 100         | 1    | ~7       | 100  | ~664       | 10,000 | 1.27e30
n = 1000        | 1    | ~10      | 1000 | ~9,966     | 1,000,000 | (unimaginable)
"""


# ------------------------------------------------------------------------------------------
# 2. Space Complexity
# ------------------------------------------------------------------------------------------
"""
Space complexity measures how much additional memory an algorithm needs as the input size 
grows. This includes:
- Auxiliary space: Extra space or temporary space used by the algorithm
- Input space: Space used to store the inputs (usually not counted unless specified)
"""

# Common Space Complexities
"""
Notation	Description	        Example
O(1)	    Constant space	    In-place array reversal
O(n)	    Linear space	    Creating a copy of an array
O(n²)	    Quadratic space	    2D matrix creation
"""


# ------------------------------------------------------------------------------------------
# How to Analyze Algorithms
# ------------------------------------------------------------------------------------------
def find_sum(arr):
    total = 0                 # O(1) operation, constant space for 'total'
    for num in arr:           # Loop runs n times
        total += num          # O(1) operation each time
    return total

# Time: O(n) - loops through each element once
# Space: O(1) - only uses a single 'total' variable


def find_duplicates(arr):
    seen = set()            # Space: will grow
    duplicates = []         # Space: will grow

    for num in arr:         # Time: O(n)
        if num in seen:     # O(1) for sets
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

# Time: O(n) - single pass through array
# Space: O(n) - 'seen' set could store up to n elements


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):                    # Outer loop: O(n)
        for j in range(0, n-i-1):         # Inner loop: O(n)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # O(1)
    return arr

# Time: O(n²) - nested loops
# Space: O(1) - sorts in-place, no extra memory


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Two recursive calls

# Time: O(2ⁿ) - each call branches into two more
# Space: O(n) - recursion stack depth


# ------------------------------------------------------------------------------------------
# Practical Tips for Optimization
# ------------------------------------------------------------------------------------------
"""
1. Measure first: Use profiling tools before optimizing
2. Focus on bottlenecks: Optimize the parts that run most frequently
3. Consider trade-offs: Sometimes trading space for time is worth it
4. Choose right data structures:
- Sets/Dictionaries: O(1) lookup vs Lists: O(n) lookup
- Arrays: Fast index access, slow inserts/deletes
- Linked Lists: Slow access, fast inserts/deletes
"""
