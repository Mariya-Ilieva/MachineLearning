def common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    common_chars = set1.intersection(set2)

    output = ''.join(common_chars)

    return output

print(common_characters('abc', 'dfab'))
print(common_characters('abеc', 'dеab'))
print(common_characters('acх', 'dfab'))
print(common_characters('abcdefa', 'defaa'))
