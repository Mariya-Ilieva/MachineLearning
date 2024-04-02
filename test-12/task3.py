def get_dummies(series):
    uniques = sorted(set(series))
    cols = {u: [] for u in uniques}

    for el in series:
        for unique in uniques:
            if el == unique:
                cols[unique].append(True)
            else:
                cols[unique].append(False)

    result = {}
    for unique in uniques:
        result[unique] = tuple(cols[unique])

    return result

s = ['a', 'b', 'a', 'c']
print(get_dummies(s))
