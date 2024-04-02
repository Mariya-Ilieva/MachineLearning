# def subarray(arr, start=None, end=None):
#     return arr[start:end]

def subarray(arr, start, end=None):
    output = []
    n = len(arr)

    if not end:
        end = n - 1

    for i in range(start, min(end + 1, n)):
        output.append(arr[i])

    return output

print(subarray([1, 2, 3, 3, 3], 2))
print(subarray([1, 2, 3, 4, 3], 2, 3))
