def includes_element(arr, el):
    result = el in arr
    return result

print(includes_element([1, 2, 3, 0, 12], 3))
print(includes_element([1, 2, 3, 0, 12], 12))
print(includes_element([1, 2, 3, 0, 12], 100))
