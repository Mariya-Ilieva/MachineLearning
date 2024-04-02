import numpy as np
from numpy.linalg import inv, qr
from numpy.random._examples.cffi.extending import rng


# arr = np.arange(10)
# np.save("some_array", arr)
# print(np.load("some_array.npy"))
# np.savez("array_archive.npz", a=arr, b=arr)
# arch = np.load("array_archive.npz")
# print(arch["b"])
# np.savez_compressed("arrays_compressed.npz", a=arr, b=arr)

# x = np.array([[1., 2., 3.], [4., 5., 6.]])
# y = np.array([[6., 23.], [-1, 7], [8, 9]])
# print(x)
# print(y)

# print(x.dot(y))
# print(np.dot(x, y))
# print(x @ np.ones(3))

# X = rng.standard_normal((5, 5))
# mat = X.T @ X
# print(inv(mat))
# print(mat @ inv(mat))

# nsteps = 1000
# rng = np.random.default_rng(seed=12345)
# draws = rng.integers(0, 2, size=nsteps)
# steps = np.where(draws == 0, 1, -1)
# walk = steps.cumsum()
# print(walk.min())
# print(walk.max())
# print((np.abs(walk) >= 10).argmax())

nwalks = 5000
nsteps = 1000
# draws = rng.integers(0, 2, size=(nwalks, nsteps)) # 0 or 1
# steps = np.where(draws > 0, 1, -1)
# walks = steps.cumsum(axis=1)
# print(walks)
# print(walks.max())
# print(walks.min())

# hits30 = (np.abs(walks) >= 30).any(axis=1)
# print(hits30)
# print(hits30.sum())
# crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)
# print(crossing_times)
# print(crossing_times.mean())

draws = 0.25 * rng.standard_normal((nwalks, nsteps))
print(draws)
