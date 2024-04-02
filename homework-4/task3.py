# def shift_positions(arr):
#     if arr:
#         result = arr.pop(0)
#     else:
#         result = None
#
#     return result

def shift_positions(arr):
    if arr:
        res = arr[0]
        arr = arr[1:]
    else:
        res = None

    return res

print(shift_positions([1, 2, 3, 0, 123]))
print(shift_positions([]))
print(shift_positions([0]))
