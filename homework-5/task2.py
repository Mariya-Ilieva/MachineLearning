# def indexOf(s1, s2, fromIndex=0):
#     end = len(s1) - len(s2)
#
#     for res in range(fromIndex, end + 1):
#         slice = res + len(s2)
#         if s1[res:slice] == s2:
#             return res
#
#     return -1

def indexOf(s1, s2, fromIndex=0):
    while fromIndex < len(s1):
        match = True
        count = 0

        while count < len(s2):
            if fromIndex + count >= len(s1) or s1[fromIndex + count] != s2[count]:
                match = False
                break
            count += 1

        if match:
            return fromIndex

        fromIndex += 1

    return -1

print(indexOf('ala bala', 'la'))
print(indexOf('github', 'hub'))
print(indexOf('microsoft', 'google'))
