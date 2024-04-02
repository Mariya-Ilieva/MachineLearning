def reverse_arr(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

def rotate(arr, n):
    if not isinstance(arr, list):
        raise TypeError(f'Please provide a valid list:{arr} is not a list')

    if not isinstance(n, int):
        raise TypeError(f'Please provide a valid number:{n} is not a number')

    if len(arr) == 0 or n == 0 or n == len(arr):
        return arr

    n = n % len(arr)

    reverse_arr(arr, 0, len(arr) - 1)
    reverse_arr(arr, 0, n - 1)
    reverse_arr(arr, n, len(arr) - 1)

def test(a, n):
    print(a, n)
    rotate(a, n)
    print(f'-> {a}')

test_data = [
    ([1, 2, 3], 1),
    ([1, 2, 3, 4], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8], 3),
    ([1, 7, 6, 11, 13, 100, 9, 101], 4)
]

for arr, n in test_data:
    test(arr, n)
