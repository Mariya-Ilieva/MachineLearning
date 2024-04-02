def lastIndexOf(arr, el, start=None):
    start = start if start else len(arr) - 1

    for res in range(start, - 1, -1):
        if arr[res] == el:
            return res

    return -1

print(lastIndexOf([1, 0, 3, 0, 12], 0))
print(lastIndexOf([1, 0, 3, 0, 12], 0, 2))
print(lastIndexOf([1, 0, 3, 0, 12], 4))
