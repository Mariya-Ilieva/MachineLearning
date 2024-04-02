# import numpy as np
#
#
# def rank(arr):
#     sorted = np.argsort(arr)
#     output = sorted.argsort() + 1
#
#     return [output]

def rank(arr):
    sorted_arr = sorted(arr)
    ranks = {num: i for i, num in enumerate(sorted_arr, 1)}
    result = [ranks[num] for num in arr]

    return result

arr = [4, 2, 7, 1]
print(rank(arr))
