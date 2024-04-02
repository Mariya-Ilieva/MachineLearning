def current_sum(arr):
    summ = 0
    return [summ := summ + n for n in arr]
#    return [sum(arr[:i+1]) for i in range(len(arr))]

print(current_sum([1, 3]))
print(current_sum([1, 2, 3]))
print(current_sum([2, -1, 8]))
print(current_sum([1, 2, 3, 4, 5]))
