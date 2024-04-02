import numpy as np


m1 = np.ones((4, 4), dtype=int)
print(m1)

m2 = np.eye(4, dtype=int)
print(m2)

m3 = np.diag([1, 2, 3, 4])
print(m3)

m4 = np.fromfunction(lambda x, y: np.where(x > y, -1, np.where(x < y, 1, 0)), (4, 4), dtype=int)
print(m4)

m5 = np.fromfunction(lambda i, j: abs(i - j), (4, 4), dtype=int)
print(m5)

m6 = np.arange(16).reshape(4, 4)
print(m6)
