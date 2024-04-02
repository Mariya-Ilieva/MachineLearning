def longest_seq(arr):
    if not isinstance(arr, list):
        raise TypeError('Input must be a list')

    longest = [arr[0]]
    temp = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            temp.append(arr[i])
        else:
            temp = [arr[i]]

        if len(temp) > len(longest):
            longest = temp

    return longest if len(longest) > 1 else None

print(longest_seq([0, 5, 1, 2, 3, 4, 5, 2, 8, 9, 10]))
print(longest_seq([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 1]))
print(longest_seq([3, 5, 7]))
print(longest_seq([3, 5, 7, 8]))
