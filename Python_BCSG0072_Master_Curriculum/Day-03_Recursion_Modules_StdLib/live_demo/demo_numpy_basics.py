# demo_numpy_basics.py
# Introduction to NumPy Vectorized Arrays and Math

import numpy as np

print("="*60)
print("           NUMPY VECTORIZED ARRAYS DEMO                   ")
print("="*60)

# Creating arrays
arr = np.arange(1, 13)
print("1D Array (1 to 12):", arr)

# Reshaping to 3x4 2D Matrix
matrix = arr.reshape(3, 4)
print("\nReshaped 3x4 Matrix:\n", matrix)

# Vectorized Operations (No loops!)
print("\nMatrix * 10:\n", matrix * 10)
print("\nMean of Matrix:", np.mean(matrix))
print("Sum of Matrix :", np.sum(matrix))
print("Sum along columns (axis 0):", np.sum(matrix, axis=0))
print("Sum along rows    (axis 1):", np.sum(matrix, axis=1))
