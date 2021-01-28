import numpy as np

n = 10
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# Two sides of the computation, depicting distributive property
res1 = np.dot(a, (b + c))
res2 = np.dot(a, b) + np.dot(a, c)

print([res1, res2])
