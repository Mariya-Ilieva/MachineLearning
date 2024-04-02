def union(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError('Please provide two valid lists')

    for el1, el2 in zip(list1, list2):
        if type(el1) != type(el2):
            raise TypeError('Cannot merge elements of different type')

    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            result.append(list2[j])
            i += 1
            j += 1

    if i < len(list1):
        result.extend(list1[i:])

    if j < len(list2):
        result.extend(list2[j:])

    return result

c1 = [1, 3, 5, 6, 7, 8]
c2 = [2, 4, 6, 8]
list_all_c = union(c1, c2)
print(list_all_c)

d1 = ['a', 'b', 'c', 'd', 'e', 'f']
d2 = ['f', 'g', 'h']
list_all_d = union(d1, d2)
print(list_all_d)
