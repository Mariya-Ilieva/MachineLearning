def repeated_str(s):
    l = len(s)

    for i in range(1, l):
        cut = ''
        for j in range(i):
            cut += s[j]

        if cut * (l // i) == s:
            return True

    return False

print(repeated_str('abc'))
print(repeated_str('1212'))
print(repeated_str('alaala'))
print(repeated_str('alaal'))
print(repeated_str('zzzzz'))
print(repeated_str('acacac'))
print(repeated_str('acaca'))
