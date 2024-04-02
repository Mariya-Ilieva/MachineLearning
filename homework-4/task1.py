def find_element(arr, el):
    try:
        i = arr.index(el)
    except ValueError:
        i = -1

    return i

print(find_element([1, 2, 3, 0, 12], 0))
print(find_element([1, 2, 3, 0, 12], 3))
print(find_element([1, 2, 3, 0, 12], 4))
