def rotate(arr, n):
    if not isinstance(arr, list):
        raise TypeError(f'Please provide a valid list:{arr} is not a list')

    if not isinstance(n, int):
        raise TypeError(f'Please provide a valid number:{n} is not a number')

    if len(arr) == 0 or n == 0 or n == len(arr):
        return arr

    n = n % len(arr)
    result = [None] * len(arr)

    for i in range(len(arr)):
        idx = (i + n) % len(arr)
        result[idx] = arr[i]

    return result

print(rotate([1, 2, 3], 1))
print(rotate([1, 2, 3, 4], 2))
print(rotate([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(rotate([1, 7, 6, 11, 13, 100, 9, 101], 4))
