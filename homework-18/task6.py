def compare(obj1, obj2):
    stack = [(obj1, obj2)]

    while stack:
        obj11, obj22 = stack.pop()

        if type(obj11) != type(obj22):
            return False

        if isinstance(obj11, (list, tuple, set)):
            if len(obj11) != len(obj22):
                return False

            stack.extend(zip(obj11, obj22))

        elif isinstance(obj11, dict):
            if len(obj11) != len(obj22):
                return False

            if obj11.keys() != obj22.keys():
                return False

            stack.extend(zip(obj11.values(), obj22.values()))

        else:
            if obj11 != obj22:
                return False

    return True


a = [[1, 2], 3, 4, 5]
b = [[1, 2], 3, 4, 5]
print(compare(a, b))  # True

a = [[3, 2], 3, 4, 5]
b = [[1, 2], 3, 4, 5]
print(compare(a, b))  # False

a = [{12, 5}, 3, 4, 5]
b = [12, 5, 3, 4, 5]
print(compare(a, b))  # False

a = [{12, 5}, 3, 4, 5]
b = [[12, 5], 3, 4, 5]
print(compare(a, b))  # False

a = [{1: [12, 14]}, 3, 4, 5]
b = [{1: [12, 14]}, 3, 4, 5]
print(compare(a, b))  # True

a = [{1: [12, 14]}, 3, 4, 5]
b = [{1: [12]}, 3, 4, 5]
print(compare(a, b))  # False

a = [{1: [12, 14]}, 3, 4, 5]
b = [{1, 12, 14}, 3, 4, 5]
print(compare(a, b))  # False

a = [{1: [12, 14]}, 3, 4, 5]
b = [{1, 12, 14}, 3, 4, 5]
print(compare(a, b))  # False

a = [(1, 2), 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(compare(a, b))  # False

a = [(1, 2), 3, 4, 5]
b = [[1, 2], 3, 4, 5]
print(compare(a, b))  # False
