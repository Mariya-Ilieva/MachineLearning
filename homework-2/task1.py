def reverse_array(arr):
    output = arr[::-1]
    return output

#reverse_array = lambda arr: [arr[i] for i in range(len(arr)-1, -1, -1)]

print(reverse_array([1, 2, 3, 4, 5, 6, 7]))
