def close_values(arr1, arr2):
    for num in arr1:
        values = [num - 1, num, num + 1]
        if not any(v in arr2 for v in values):
            return False

    for num in arr2:
        values = [num - 1, num, num + 1]
        if not any(v in arr1 for v in values):
            return False

    return True

print(close_values([1, 3, 5], [2, 4, 6]))
print(close_values([1, 3, 5], [2, 4]))
print(close_values([1, 3, 5], [2]))
print(close_values([1, 3, 5], [2, 4, 7]))
