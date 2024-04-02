import numpy as np
from numpy.random._examples.cffi.extending import rng


# arr = np.arange(10)
# print(arr)
# print(np.sqrt(arr))
# print(np.exp(arr))

# x = rng.standard_normal(8)
# y = rng.standard_normal(8)
# print(x)
# print(y)
# print(np.maximum(x, y))

# arr1 = rng.standard_normal(7) * 5
# print(arr1)
# remainder, whole_part = np.modf(arr1)
# print(remainder)
# print(whole_part)

# print(np.add(arr1, 1))
# print(np.add(arr1, 1, out=arr1))

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs, ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])
# result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
# print(result)
# result = np.where(cond, xarr, yarr)
# print(result)
# arr = rng.standard_normal((4, 4))
# print(arr)
# print(arr > 0)
# print(np.where(arr > 0, 2, -2))
# print(np.where(arr > 0, 2, arr))

# arr = rng.standard_normal((5, 4))
# print(arr)
# print(arr.mean())
# print(np.mean(arr))
# print(arr.sum())
# print(arr.mean(axis=1))
# print(arr.sum(axis=0))

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
# print(arr.cumsum())

# arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(arr)
# print(arr.cumsum(axis=0))
# print(arr.cumsum(axis=1))

# arr = rng.standard_normal(100)
# print((arr > 0).sum())
# print((arr <= 0).sum())
# bools = np.array([False, False, True, False])
# print(bools.any())
# print(bools.all())

# arr = rng.standard_normal(6)
# print(arr)
# arr.sort()
# print(arr)
# arr = rng.standard_normal((5, 3))
# print(arr)
# arr.sort(axis=0)
# print(arr)
# arr.sort(axis=1)
# print(arr)
# arr2 = np.array([5, -10, 7, 1, 0, -3])
# sorted_arr2 = np.sort(arr2)
# print(sorted_arr2)

names = np.array(["Bob", "Will", "Joe", "Bob", "Will", "Joe", "Joe"])
print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
print(sorted(set(names)))
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
