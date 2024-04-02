def split(s, sep = ''):
    if not isinstance(s, str):
        raise TypeError(f'Please provide a valid string, {s} is not a string.')

    # piece = ''
    #
    # for el in s:
    #     if el == sep:
    #         yield piece
    #         piece = ''
    #     else:
    #         piece += el
    #
    # yield piece

    i = 0
    while (j := s.find(sep, i)) != -1:
        yield s[i:j]

        i = j + len(sep)

    yield s[i:]

d = '12-05-2005'
for date_part in split(d, '-'):
    print(date_part)

m = 'I, am, programmer'
for sentence_part in split(m, ', '):
    print(sentence_part)
