def remove_duplicates(arr):
    current = set()
    output = []

    for n in arr:
        if n not in current:
            current.add(n)
            output.append(n)

    return output

print(remove_duplicates([1, 3, 8, 1, 16, 3, 4]))
print(remove_duplicates([15, 1, 165, 87, 6, 13, 15]))
print(remove_duplicates([100, 200, 300, 400, 300, 200, 100]))
