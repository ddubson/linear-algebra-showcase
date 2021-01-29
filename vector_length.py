import numpy as np

v1 = np.array([1, 2, 3, 4, 5, 6])

# Method 1: regular dot product
vl1 = np.sqrt(np.dot(v1, v1))

# Method 2: take the norm
vl2 = np.linalg.norm(v1)

print(vl1, vl2)
