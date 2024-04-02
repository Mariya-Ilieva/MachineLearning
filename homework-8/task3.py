def remove_elements(s, *el):
    for e in el:
        if e not in s:
            return 'The symbol you provided is not correct'

    output = ''
    for l in s:
        if l not in el:
            output += l

    return output

print(remove_elements('alabala', 'a', 'b'))
print(remove_elements('abracadabra', 'b', 'r', 'c'))
print(remove_elements('hello', 'u'))
