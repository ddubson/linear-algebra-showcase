import numpy as np


def commutativity(row1: int, row2: int) -> None:
    print(row1)
    print(row2)
    dot1 = np.dot(row1, row2)
    dot2 = np.dot(row2, row1)
    assert dot1 == dot2
    print(dot1)
    print(dot2)


# Generate two 100-element random row vectors, compute dot product
# a with b, b with a
row1 = np.random.randint(100, size=100)
row2 = np.random.randint(100, size=100)
commutativity(row1, row2)

# Generate two 2-element integer row vectors
row1 = np.random.randint(100, size=2)
row2 = np.random.randint(100, size=2)
commutativity(row1, row2)
