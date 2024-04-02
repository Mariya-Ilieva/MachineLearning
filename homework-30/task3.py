def get_float_parts(num):
    if not isinstance(num, float):
        raise TypeError('Please provide a valid float number')

    if num == 0:
        return 0, 0

    sign = 1 if num > 0 else -1
    num = abs(num)

    e = 0
    while abs(num) < 1:
        num *= 10
        e -= 1

    while abs(num) >= 10:
        num /= 10
        e += 1

    return sign * num, e

x = 0.00031345
mantissa, exponent = get_float_parts(x)
print(mantissa, exponent)

x = 3134.5
mantissa, exponent = get_float_parts(x)
print(mantissa, exponent)
