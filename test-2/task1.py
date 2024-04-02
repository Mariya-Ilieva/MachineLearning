def compare(l1, l2):
    for i in l1:
        if i not in l2:
            return False

    for i in l2:
        if i not in l1:
            return False

    return True

print(compare([1, 5, 7, 8, 13], [13, 5, 7, 1, 8]))
print(compare([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(compare([1, 2, 2, 2, 3, 4], [1, 2, 3]))
print(compare([100, 150, 100, 150, 100, 150], [150, 100]))
