import numpy as np

n = 10
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# Two sides of the computation, depicting lack of associativity
res1 = np.dot(a, np.dot(b, c))
res2 = np.dot(np.dot(a, b), c)

print([res1, res2])
