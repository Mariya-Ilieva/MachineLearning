def convert_hex(n):
    if n == 0:
        return '0'

    hex_digits = '0123456789abcdef'
    hex_result = ''

    while n > 0:
        digit = n % 16
        hex_result = hex_digits[digit] + hex_result
        n //= 16

    return hex_result

print(convert_hex(5))
print(convert_hex(10))
print(convert_hex(16))
print(convert_hex(255))
print(convert_hex(27))
