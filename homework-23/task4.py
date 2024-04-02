import sys


def second_smallest(s):
    smallest1 = sys.maxsize
    smallest2 = sys.maxsize

    for ch in s:
        if ch.isdigit():
            n = int(ch)

            if n < smallest1:
                smallest2 = smallest1
                smallest1 = n
            elif smallest1 < n < smallest2:
                smallest2 = n

    return smallest2 if smallest2 != sys.maxsize else -1

print(second_smallest('3dm1o24'))
print(second_smallest('alabala'))
print(second_smallest('1git1hub'))
