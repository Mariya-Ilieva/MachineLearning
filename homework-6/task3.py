def common_characters(str1, str2):
    chars = {}

    for ch in str1:
        if ch in str2 and ch not in chars:
            chars[ch] = None

    return ''.join([char for char in chars.keys()])


print(common_characters('abc', 'def'))
print(common_characters('abc', 'cde'))
print(common_characters('abc', 'dafc'))
print(common_characters('abcaf', 'debafa'))
