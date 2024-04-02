import numpy as np
from numpy import array


# my_arr = np.arange(1_000_000)
# my_list = list(range(1_000_000))
# my_arr2 = my_arr * 2
# my_list2 = [x * 2 for x in my_list]
# print(my_arr2, my_list2)

# data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
# print(data, data*10, data + data)
# print(data.shape)
# print(data.dtype)

# data1 = [6, 7.5, 8, 0, 1]
# arr1 = np.array(data1)
# print(arr1)

# data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# arr2 = np.array(data2)
# print(arr2, arr2.ndim, arr2.shape)
# print(arr1.dtype, arr2.dtype)

# arr = np.zeros(10)
# print(arr)
# print(np.zeros((3, 6)))
# print(np.empty((2, 3, 2)))
# print(np.arange(15))

# arr1 = np.array([1, 2, 3], dtype=np.float64)
# arr2 = np.array([1, 2, 3], dtype=np.int32)
# print(arr1.dtype)
# print(arr2.dtype)

# arr = np.array([1, 2, 3, 4, 5])
# print(arr.dtype)
# float_arr = arr.astype(np.float64)
# print(float_arr.dtype)

# arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
# print(arr)
# print(arr.astype(np.int32))
# numeric_strings = np.array(["1.25", "-9.6", "42"], dtype=np.string_)
# numeric_strings.astype(float)
# print(numeric_strings)

# int_array = np.arange(10)
# calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
# int_array.astype(calibers.dtype)
# print(int_array)
# zeros_uint32 = np.zeros(8, dtype="u4")
# print(zeros_uint32)

# arr = np.array([[1., 2., 3.], [4., 5., 6.]])
# print(arr, arr * arr, arr - arr, 1 / arr, arr ** 2)
# arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
# print(arr2)
# print(arr2 > arr)

# arr = np.arange(10)
# print(arr, arr[5])
# print(arr[5:8])
# arr[5:8] = 12
# print(arr)

# arr_slice = arr[5:8]
# arr_slice[1] = 12345
# print(arr)
# arr_slice[:] = 64
# print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2d[0][2])
# print(arr2d[0, 2])

# arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3d[0])
# old_values = arr3d[0].copy()
# arr3d[0] = 42
# print(arr3d)
# arr3d[0] = old_values
# print(arr3d)
# print(arr3d[1, 0])
# x = arr3d[1]
# print(x, x[0])

arr = array([ 0, 1, 2, 3, 4, 64, 64, 64, 8, 9])
print(arr[1:6])
print(arr2d, arr2d[:2])
print(arr2d[:2, 1:])
lower_dim_slice = arr2d[1, :2]
print(lower_dim_slice.shape)
print(arr2d[:2, 2])
print(arr2d[:, :1])
arr2d[:2, 1:] = 0
print(arr2d)
