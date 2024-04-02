def remove_el(s, idx):
    if idx < 0 or idx >= len(s):
        return f'The position you provided is not correct, it must be between 0 and {len(s)-1}'

    output = ''
    for i in range(len(s)):
        if i != idx:
            output += s[i]

    return output

print(remove_el('alabala', 2))
print(remove_el('abracadabra', 3))
print(remove_el('hello', 5))
