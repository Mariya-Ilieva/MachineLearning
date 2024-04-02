def find_element(arr, el, start_pos):
    try:
        i = arr.index(el, start_pos)
    except ValueError:
        i = -1
    return i

print(find_element([1, 2, 3, 0, 12], 0, 2))
print(find_element([1, 2, 3, 0, 12], 3, 3))
print(find_element([1, 2, 3, 0, 12], 4, 1))
