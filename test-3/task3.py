def remove_duplicates(arr):
    i = len(arr) - 1

    while i > 0:
        if arr[i] in arr[:i]:
            arr.pop(i)

        i -= 1

    return arr

print(remove_duplicates([3, 12, 5, 12, 8, 5, 12, 12]))
print(remove_duplicates([1, 2, 3, 2, 1]))
