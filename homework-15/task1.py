def splice(arr, start, count=None, *args):
    if start < 0 or start >= len(arr):
        raise ValueError('Invalid start position')

    if not count:
        count = len(arr) - start

    if count < 0 or start + count > len(arr):
        raise ValueError('Invalid count of elements to remove')

    deleted = []
    for _ in range(count):
        deleted.append(arr.pop(start))

    for i, el in enumerate(args):
        arr.insert(start + i, el)

    return deleted

print(splice([1, 2, 3, 4], 1, 1))
print(splice([1, 2, 3, 4], 1, 2, 5, 6))
print(splice([1, 2, 3, 4], 1))
print(splice([1, 2, 3, 4], 2, 2, 7, 8, 9))
