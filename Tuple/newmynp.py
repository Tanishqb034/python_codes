import numpy as np

a = np.array([10, 20, 30, 40])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(matrix)

print(matrix.ndim)   # Number of dimensions: 2
print(matrix.shape)  # (2, 3)
print(matrix.size)   # 6 elements
print(matrix.dtype)  # Data type