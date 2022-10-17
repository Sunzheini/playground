# 1. Bombs

# from collections import deque
#
#
# def check_if_match(a, b):
#     current_sum = a + b
#     for i in bombs.keys():
#         if current_sum == bombs[i]:
#             pouch[i] += 1
#
#
# def check_if_three_of_a_type():
#     for kk in pouch:
#         if pouch[kk] == 3:
#             return True
#     return False
#
#
# bomb_effects = deque([int(x) for x in input().split(', ')])
# bomb_casings = [int(x) for x in input().split(', ')]
# pouch = {
#     'Datura Bombs': 0,
#     'Cherry Bombs': 0,
#     'Smoke Decoy Bombs': 0,
# }
#
# bombs = {
#     'Datura Bombs': 40,
#     'Cherry Bombs': 60,
#     'Smoke Decoy Bombs': 120,
# }
#
#
# while bomb_effects and bomb_casings and not check_if_three_of_a_type():
#     current_bomb_effect = bomb_effects.popleft()
#     current_bomb_casing = bomb_casings.pop()
#
#     if not check_if_match(current_bomb_effect, current_bomb_casing):
#         bomb_effects.appendleft(current_bomb_effect)
#         bomb_casings.append(current_bomb_casing-5)
#
#
# if check_if_three_of_a_type():
#     print("Bene! You have successfully filled the bomb pouch!")
# else:
#     print("You don't have enough materials to fill the bomb pouch.")
#
#
# if not bomb_effects:
#     print("Bomb Effects: empty")
# else:
#     print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
#
# if not bomb_casings:
#     print("Bomb Casings: empty")
# else:
#     print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
#
# print(pouch)


# 2. Minesweeper Generator

# def is_outside(row, col):
#     return row < 0 or col < 0 or row >= matrix_size or col >= matrix_size
#
#
# def count_neighboring_bombs(row, col):
#     counter = 0
#
#     for kk in directions.values():
#         crow, ccol = kk(row, col)
#         if not is_outside(crow, ccol) and matrix[crow][ccol] == '*':
#             counter += 1
#
#     return counter
#
#
# matrix_size = int(input())
# number_of_bombs = int(input())
#
# directions = {
#     'R': lambda r, c: (r, c + 1),
#     'L': lambda r, c: (r, c - 1),
#     'U': lambda r, c: (r - 1, c),
#     'D': lambda r, c: (r + 1, c),
#     'NW': lambda r, c: (r - 1, c - 1),
#     'NE': lambda r, c: (r - 1, c + 1),
#     'SE': lambda r, c: (r + 1, c - 1),
#     'SW': lambda r, c: (r + 1, c + 1),
# }
#
# matrix = []
#
# for i in range(matrix_size):
#     matrix.append([0 for x in range(matrix_size)])
#
# for j in range(number_of_bombs):
#     positions = input()
#     bomb_row, bomb_col = int(positions[1]), int(positions[4])
#     matrix[bomb_row][bomb_col] = '*'
#
#
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         if matrix[row][col] == '*':
#             continue
#         cell_value = count_neighboring_bombs(row, col)
#         matrix[row][col] = cell_value
#
#
# for l in matrix:
#     print(*l, sep=' ')


# 3. Flights

# def flights(*args):
#     my_dict = {}
#
#     for i in range(0, len(args)-1, 2):
#         if args[i] == 'Finish':
#             return my_dict
#
#         current = args[i]
#         next_one = int(args[i+1])
#
#         if current not in my_dict:
#             my_dict[current] = 0
#         my_dict[current] += next_one
#
#     return my_dict
#
#
# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98,
#               'Paris', 115, 'Finish', 'Paris', 15))
#
# print(flights('London', 0, 'New York', 9, 'Aberdeen',
#               215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
#
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
