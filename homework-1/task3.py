def array_sorted(arr):
    output = []

    for value in range(1, 6):
        for num in arr:
            if num == value:
                output.append(num)

    return output

'''def array_sorted(arr):
    return [num for value in range(1, 6) for num in arr if num == value]'''

'''def array_sorted(arr):
    return sorted(arr, key=lambda x: (x, arr.count(x)))'''

print(array_sorted([2, 3, 5, 5, 1, 3, 2, 5, 4]))
