import numpy as np

# Create 2 4x6 matrices of random numbers
matrix1 = np.random.randint(100, size=(4, 6))
matrix2 = np.random.randint(100, size=(4, 6))

# Use a for-loop to compute dot products between corresponding columns
dot_product_matrix = np.full((4, 6), np.inf)

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        dot_product_matrix[i][j] = np.dot(matrix1[i][j], matrix2[i][j])

print(matrix1)
print(matrix2)
print(dot_product_matrix)
