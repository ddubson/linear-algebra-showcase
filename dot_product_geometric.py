import numpy as np
import matplotlib.pyplot as plt

# Vector 1
v1 = np.array([2, 4, -3])
# Vector 2
v2 = np.array([0, -3, -3])
# Angle between the two vectors from the standard position
# vector norm is vector length (i.e. ||v||)
ang = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], 'b')
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], 'r')

plt.axis((-6, 6, -6, 6))
plt.title('Angle between vectors: %s rad.' % ang)
plt.show()

vx = np.array([16, -2, 4])
vy = np.array([.5, 2, -1])
costheta = np.dot(vx, vy) / (np.linalg.norm(v1) * np.linalg.norm(v2))
print(costheta)

va = np.array([1, -2])
vb = np.array([2, 3])
vc = np.array([0, 2])
print(np.dot(va, vb))
print(np.dot(va, vc))
print(np.dot(vb, vc))
