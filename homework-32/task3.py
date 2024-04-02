import re


def decompose(literal):
    match = re.search(r'([+\-]?\d*\.?\d+)(?:[eE]([+\-]?\d+))?', literal)

    if match is None:
        raise ValueError('Invalid float literal')

    mantissa, exponent = match.groups()
    exponent = 0 if exponent is None else int(exponent)

    sign = abs(float(mantissa)) / float(mantissa)
    mantissa = float(mantissa) * float(sign)

    while mantissa >= 10:
        mantissa /= 10
        exponent += 1

    while mantissa < 1:
        mantissa *= 10
        exponent -= 1

    return sign * mantissa, exponent

values = ['.1', '1.5', '3', '-12', '25', '1000', '12.3e-2']

for v in values:
    mantissa, exponent = decompose(v)
    print(f'({mantissa}, {exponent})')
