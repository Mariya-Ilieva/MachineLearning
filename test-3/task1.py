def appears_most_often(arr):
    result = {}

    for n in arr:
        if n in result:
            result[n] += 1
        else:
            result[n] = 1

    output = []
    result = sorted(result.items(), key=lambda x: (-x[1], x[0]))

    for k, v in result:
        output.extend([k] * v)

    return output

print(appears_most_often([2, 3, 5, 3, 7, 9, 5, 3, 7]))
print(appears_most_often([2, 1, 2]))
print(appears_most_often([1, 1, 2, 2]))
