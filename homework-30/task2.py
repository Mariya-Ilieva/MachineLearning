def remove_all(lst1, lst2):
    if not isinstance(lst1, list) or not isinstance(lst2, list):
        raise TypeError('Please provide two valid lists')

    i1 = 0
    i2 = 0
    set_lst2 = set(lst2)

    while i1 < len(lst1) and lst1[i1] not in set_lst2:
        i1 += 1

    i1 = i2
    while i1 < len(lst1):
        if lst1[i1] not in lst2:
            lst1[i2] = lst1[i1]
            i2 += 1

        i1 += 1

    for _ in range(len(lst1) - i2):
        lst1.pop()

def retain_all(lst1, lst2):
    if not isinstance(lst1, list) or not isinstance(lst2, list):
        raise TypeError('Please provide two valid lists')

    i1 = 0
    i2 = 0
    set_lst2 = set(lst2)

    while i1 < len(lst1) and lst1[i1] in set_lst2:
        i1 += 1

    i1 = i2
    while i1 < len(lst1):
        if lst1[i1] in lst2:
            lst1[i2] = lst1[i1]
            i2 += 1

        i1 += 1

    for _ in range(len(lst1) - i2):
        lst1.pop()

c1 = [1, 2, 3, 4, 5]
c2 = [3, 5, 7]
print(c1)
remove_all(c1, c2)
print(c1)

d1 = [1, 2, 3, 4, 5]
d2 = [3, 5, 7]
print(d1)
retain_all(d1, d2)
print(d1)
