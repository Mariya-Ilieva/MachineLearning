def includes_element(arr, el, start_pos):
    result = el in arr[start_pos:]
    return result

print(includes_element([1, 2, 3, 0, 12], 3, 3))
print(includes_element([1, 2, 3, 0, 12], 12, 2))
print(includes_element([1, 2, 3, 0, 12], 100, 1))
