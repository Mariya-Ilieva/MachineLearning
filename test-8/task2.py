import sys


def sort_arr(arr):
    if not isinstance(arr, list):
        raise TypeError('Please provide a valid list')

    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError('All elements must be valid numbers')

    n = len(arr)
    min_i = 0
    max_i = n - 1
    i = 0

    while i < n // 2:
        min_n = sys.maxsize
        max_n = - sys.maxsize

        j = i
        while j < n - i:
            if arr[j] < min_n:
                min_n = arr[j]
                min_i = j

            if arr[j] > max_n:
                max_n = arr[j]
                max_i = j

            j += 1

        arr[i], arr[max_i] = arr[max_i], arr[i]

        if min_i == i:
            min_i = max_i

        arr[n - i - 1], arr[min_i] = arr[min_i], arr[n - i - 1]

        i += 1


a1 = [1, 5, 7, 5, 8, 2, 6]
sort_arr(a1)
print(a1)

a2 = [55, 44, 100, 200, 3, 8]
sort_arr(a2)
print(a2)
