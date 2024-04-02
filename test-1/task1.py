def biggest_nums(arr, k):
    if k > len(arr):
        raise ValueError('ERROR')

    output = []
    current = arr.copy()

    for _ in range(k):
        max_value = max(current)
        output.append(max_value)
        current.remove(max_value)

    return set(output)

print(biggest_nums([1, 8, 0, 6, 3, 6], 3))
print(biggest_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(biggest_nums([2, 4, 8, 64, 128], 3))
