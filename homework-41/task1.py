def find(arr, target, left=None, right=None):
    if left is None:
        left = 0

    if right is None:
        right = len(arr) - 1

    if left > right:
        return [-1, -1]

    mid = (left + right) // 2

    if arr[mid] == target:
        start = find(arr, target, left, mid - 1)
        end = find(arr, target, mid + 1, right)

        if start[0] != -1:
            start_index = start[0]
        else:
            start_index = mid

        if end[1] != -1:
            end_index = end[1]
        else:
            end_index = mid

        return [start_index, end_index]
    elif arr[mid] < target:
        return find(arr, target, mid + 1, right)
    else:
        return find(arr, target, left, mid - 1)

a = [1, 2, 3, 3, 3, 5, 8]
print(find(a, 3))

a = [1, 1, 2, 3, 4, 5, 8]
print(find(a, 3))

a = [1, 1, 2, 3, 4, 5, 8]
print(find(a, 6))
