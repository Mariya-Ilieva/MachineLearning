def compare_str(s1, s2):
    c1 = 0
    c2 = 0

    while c1 < len(s1) and c2 < len(s2):
        if s1[c1] == ' ':
            c1 += 1
            continue
        if s2[c2] == ' ':
            c2 += 1
            continue
        if s1[c1].lower() != s2[c2].lower():
            return False

        c1 += 1
        c2 += 1

    while c1 < len(s1) and s1[c1] == ' ':
        c1 += 1

    while c2 < len(s2) and s2[c2] == ' ':
        c2 += 1

    return c1 == len(s1) and c2 == len(s2)

# def compare_str(s1, s2):
#     if len(s1) < len(s2):
#         s1, s2 = s2, s1
#
#     len_used = len(s1)
#     idx = 0
#
#     for i in range(len_used):
#         if s1[i] == ' ':
#             continue
#         if s1[i].lower() not in s2.lower():
#             return False
#         if s1[i].lower() == s2[idx].lower():
#             idx += 1
#
#     return True

print(compare_str('  a bc  ', 'abc'))
print(compare_str('ABC', 'abc'))
print(compare_str(' ala   bala', 'ala Bala'))
print(compare_str(' ала bala  ', 'alabala'))
