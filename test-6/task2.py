def isNum(s):
    if not s or not isinstance(s, str):
        raise TypeError('Please provide a valid string')

    point = False
    exponent = False

    idx_e = 0

    for i, el in enumerate(s):
        if '0' <= el <= '9':
            continue

        if el == '.':
            if point or exponent:
                return False

            point = True

        elif el == 'e':
            if exponent or i == 0:
                return False

            if i == len(s) - 1 or not('0' <= s[i + 1] <= '9' or s[i + 1] == '-' or el == '+'):
                return False

            exponent = True

            idx_e = i

        elif el == '-' or el == '+':
            if i == 0:
                continue

            if idx_e != i - 1:
                return False

        else:
            return False

    if not s:
        return False

    return True


test_data = [
    ('0', True),
    ('0.1', True),
    ('abc', False),
    ('1 a', False),
    ('2e10', True),
    ('1.234e2', True),
    ('1.2e2.5', False),
    ('1e-2', True),
    ('e-2', False)
]

for data, expected in test_data:
    result = isNum(data)
    if expected != result:
        print(f'With {data} returned {result} but expected {expected}')
