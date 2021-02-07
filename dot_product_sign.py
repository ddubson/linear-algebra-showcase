import numpy as np

# Goal: test whether the dot product sign is invariant to scalar multiplication

# Generate two vectors (R3)
v1 = np.array([-3, 4, 5])
v2 = np.array([3, 6, -3])

# Generate two scalars
s1 = 2
s2 = 3

# Compute the dot product between vectors
dp1 = np.dot(v1, v2)

# Compute the dot product between the scaled vectors
dp2 = np.dot(v1 * s1, v2 * s2)

print(f"Original dot product: {dp1}")
print(f"Scaled dot product:   {dp2}")
