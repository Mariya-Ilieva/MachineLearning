# def same_numbers(arr1, arr2):
#     return set(arr1) == set(arr2)

def same_numbers(arr1, arr2):
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] != arr2[j]:
            return False

        while i < len(arr1) - 1 and arr1[i] == arr1[i + 1]:
            i += 1
        while j < len(arr2) - 1 and arr2[j] == arr2[j + 1]:
            j += 1

        i += 1
        j += 1

    return i == len(arr1) and j == len(arr2)

print(same_numbers([1, 1, 2, 3], [1, 2, 2, 2, 3]))
print(same_numbers([1, 2, 3, 3, 3], [2, 2, 2, 4]))
