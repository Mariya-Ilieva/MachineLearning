# def insert_element(arr, el):
#     arr.insert(0, el)
#
#     return arr

def insert_element(arr, el):
    if arr:
        arr = [el] + arr
    else:
        arr = [el]

    return arr

print(insert_element([1, 2, 3, 0, 123], 8))
print(insert_element([], 1))
print(insert_element([0], 7))
