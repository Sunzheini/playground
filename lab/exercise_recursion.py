# ------------------------------------------------------------------
# 1. Recursion: a function that calls itself
# ------------------------------------------------------------------

# factorial definition is x!= x * (x-1) * (x-2) * (x-3) ... 1.
def factorial(n: int) -> int:
    """Returns the factorial of n."""
    if n == 0:            # Base case for recursion (дъно)
        return 1

    return n * factorial(n - 1)     # Recursive case


# ----------------------------------------------------------------

# Fibonacci sequence: a sequence where each number is the sum of the
# two preceding ones, usually starting with 0 and 1.
# F(n) = F(n-1) + F(n-2), where F(n) represents the nth Fibonacci number.
def array_sum_calculation(my_list):
    """Returns the sum of all elements in the list."""
    if not my_list:                 # Base case: if the list is empty
        return 0

    return my_list[0] + array_sum_calculation(my_list[1:])


# print(factorial(5))  # Output: 120
# print(array_sum_calculation([5, 4, 3, 2, 3]))

# ------------------------------------------------------------------
# 2. Pre-actions, Recursion, Post-actions
# ------------------------------------------------------------------

# Drawing: A recursive function that prints a drawing with n lines.
def drawing(n: int) -> None:
    """Returns a string representation of a drawing with n lines."""
    symbol = '*'

    if n == 0:
        return

    # Pre-action
    print(n * symbol)

    # Recursion
    drawing(n - 1)

    # Post-action
    symbol = '#'
    print(n * symbol)


# -------------------------------------------------------------------

# Vector generation: Generate all possible n-bit vectors.
def gen01(index, vector):
    if index >= len(vector):
        print(vector)
        return

    for num in range(2):
        vector[index] = num
        gen01(index=index+1, vector=vector)


def generate_all_possible_n_bit_vectors(n: int) -> None:
    vector = n * [0]
    gen01(index=0, vector=vector)


# drawing(5)
# generate_all_possible_n_bit_vectors(5)

# ------------------------------------------------------------------
# 3. Backtracking: A technique for solving problems incrementally, trying partial solutions and then abandoning them if they are not valid.
# ------------------------------------------------------------------

# Find all paths in a labyrinth (maze) from start to end.
def find_all_paths(row, col, labyrinth, direction, path):
    if row < 0 or row >= len(labyrinth) or col < 0 or col >= len(labyrinth[0]):
        return

    if labyrinth[row][col] == '*':      # Wall
        return

    if labyrinth[row][col] == 'v':      # Already visited
        return

    # Add the current cell to the path
    path.append(direction)

    if labyrinth[row][col] == 'e':      # End of the path
        print(''.join(path))
    else:
        # Mark the current cell as visited
        labyrinth[row][col] = 'v'

        # Explore all four directions: down, up, right, left
        find_all_paths(row + 1, col, labyrinth, 'D', path)  # Go Down
        find_all_paths(row - 1, col, labyrinth, 'U', path)  # Go Up
        find_all_paths(row, col + 1, labyrinth, 'R', path)  # Go Right
        find_all_paths(row, col - 1, labyrinth, 'L', path)  # Go Left
        labyrinth[row][col] = '-'

    # Unmark the current cell (backtrack)
    path.pop()


def get_labyrinth_info(rows, cols, matrix):
    labyrinth = []
    path = []

    for row in range(rows):
        labyrinth.append(matrix[row].split(' '))

    find_all_paths(0, 0, labyrinth, '', path)


# get_labyrinth_info(3, 3, ['- - -', '- * -', '- - e'])


# ------------------------------------------------------------------

# 8- Queens problem: Place 8 queens on a chessboard such that no two queens threaten each other.


















