import numpy as np

matrix = np.array([[3, 0, -1],
                   [2, -2, 3],
                   [-1, 2, 5]])

mat_det = round(np.linalg.det(matrix))
mat_rev = np.linalg.inv(matrix)

print(matrix)
print(mat_det)
print(mat_rev * mat_det)
