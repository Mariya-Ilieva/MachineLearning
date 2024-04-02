def union(set1, set2):
    output = set(set1)

    for el in set2:
        if el not in output:
            output.add(el)

    return output

def intersect(set1, set2):
    output = set()

    # for el in set1:
    #     if el in set2:
    output.update(el for el in set1 if el in set2)

    return output

def diff(set1, set2):
    output = set()

    for el in set1:
        if el not in set2:
            output.add(el)

    return output

def symmetrical_diff(set1, set2):
    output = set()

    output.update(el for el in set1 if el not in set2)
    output.update(el for el in set2 if el not in set1)

    return output

print(union((1, 2, 3, 4, 5), (4, 5, 6, 7, 8)))
print(intersect((1, 2, 3, 4, 5), (4, 5, 6, 7, 8)))
print(diff((1, 2, 3, 4, 5), (4, 5, 6, 7, 8)))
print(symmetrical_diff((1, 2, 3, 4, 5), (4, 5, 6, 7, 8)))
