def remove_repetition(arr_sort):
    output = []

    for n in arr_sort:
        if not output or n != output[-1]:
            output.append(n)

    return output

print(remove_repetition([1, 2, 3, 3, 4, 4, 5]))
print(remove_repetition([]))
print(remove_repetition([1, 3, 3, 5, 7, 7, 9, 150, 200, 200, 200, 200, 200]))
