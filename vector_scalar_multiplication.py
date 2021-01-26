import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([3, -1])  # vector
lam = -.3  # scalar
v1m = v1 * lam  # scalar-modulated

plt.plot([0, v1[0]], [0, v1[1]], 'b', label="v_1")
plt.plot([0, v1m[0]], [0, v1m[1]], 'r:', label="\lambda v_1")

plt.axis('square')
axlim = max([
    abs(max(v1)),
    abs(max(v1m))
]) * 1.5  # Dynamic axis lim

plt.axis((-axlim, axlim, -axlim, axlim))
plt.grid()
plt.show()
