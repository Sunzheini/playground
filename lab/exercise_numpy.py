# NumPy


# matrix: faster than lists, can do lots more
import numpy as np


# a = np.array([1, 2, 3, 4, 5])       # [1 2 3 4 5]
# b = [1, 2, 3, 4, 5]
# print(a)
# print(b)


# a = np.array([1, 2, 3, 4, 5], dtype='int8')
# print(a.dtype)


# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a)
# print(a[1, 3])                      # 8
# print(a[1, -2])                     # 7
# print(a[0, :])                      # [1 2 3 4]


# a = np.zeros(5, int)                       # [0 0 0 0 0]
# print(a)


# a = np.full((2, 2), 99, int)                # 2 x 2 matrix with 99s
# print(a)


# a = np.full((2, 2), 'a')                # 2 x 2 matrix with 'a'
# print(a)


a = np.full((2, 2), 'a')                # 2 x 2 matrix with 'a'
print(f"{a}")















