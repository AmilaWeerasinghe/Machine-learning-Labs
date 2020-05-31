# include all TryOut in Numpy section
import numpy as np  # import numpy module as np

a = np.array([1, 2, 3])  # Creating 1D array
matrix = np.array([np.arange(3), [i for i in range(1, 4)], [6, 7, 8]])
#mt = np.zeros((5, 2, 2), dtype=float)
#mt = np.ones(4, 5)
#mt = matrix[1, 0]
#matrix[0] = 42
#mt = matrix[1:3]
# mt = matrix[]
#mt = matrix[1:]#
#mt = matrix[1:100]
#mt = matrix[:]

#mt = matrix[1:, :2]
#mt = matrix.ravel()
#mt = matrix[:, 1]. copy()
#t = matrix[1]. tolist()
# matrix.reshape(−1)
#mt = np.sqrt(matrix)
#mt = np.exp(matrix)
#mt = np.min(matrix)
#mt = np.max(matrix, axis=1)
#mt = np.min(np.maximum(np.random.randn(4), np.random.randn(4)))
#mt = np.mean(matrix)
#mt = np.mean(matrix, axis=0)
#mt = np.sum(matrix)
#mt = np.invert(matrix)
#mt = np.random.randn(5)
mt = np.trace(matrix)
print(mt)
