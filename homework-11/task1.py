def compare_str(s1, s2):
    s1 = s1.strip().lower()
    s2 = s2.strip().lower()

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    len_used = len(s1)
    idx = 0
    c = 0

    for i in range(len_used):
        if s1[i] == ' ':
            c += 1
            if c > 1:
                continue
        if s1[i].lower() not in s2.lower():
            return False
        if s1[i].lower() == s2[idx].lower():
            idx += 1

    return True

print(compare_str('  ab c  ', 'abc'))
print(compare_str('ABC', 'abc'))
print(compare_str(' ала bala  ', 'alabala'))
