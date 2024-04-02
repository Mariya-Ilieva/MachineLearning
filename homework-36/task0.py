import numpy as np
from random import normalvariate


names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])
# print(names)
# print(data)

# print(names == "Bob")
# print(data[names == "Bob"])
# print(data[names == "Bob", 1:])
# print(data[names == "Bob", 1])
# print(names != "Bob")

# print(~(names == "Bob"))
# print(data[~(names == "Bob")])

# cond = names == "Bob"
# print(data[~cond])

# mask = (names == "Bob") | (names == "Will")
# print(mask)
# print(data[mask])
# data[data < 0] = 0
# print(data)

# data[names != "Joe"] = 7
# print(data)

arr = np.zeros((8, 4))
# for i in range(8):
#     arr[i] = i
# print(arr)

# print(arr[[4, 3, 0, 6]])
# print(arr[[-3, -5, -7]])

# arr = np.arange(32).reshape((8, 4))
# print(arr)

# print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
# print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
# print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

# arr[[1, 5, 7, 2], [0, 3, 1, 2]] = 0
# print(arr)

# arr = np.arange(15).reshape((3, 5))
# print(arr)

# arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])
# print(arr)

# print(np.dot(arr.T, arr))
# print(arr.T @ arr)
# print(arr)
# print(arr.swapaxes(0, 1))

# samples = np.random.standard_normal(size=(4, 4))
# print(samples)

# N = 1_000_000
# samples = [normalvariate(0, 1) for _ in range(N)]
# print(samples)
# print(np.random.standard_normal(N))

# rng = np.random.default_rng(seed=12345)
# data = rng.standard_normal((2, 3))
# print(type(rng))
# print(np.random._generator.Generator)
