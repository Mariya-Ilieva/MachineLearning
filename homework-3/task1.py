def format_ip(n):
    output = ''

    for _ in range(4):
        digit = n % 256
        output = str(digit) + '.' + output
        n //= 256

    return output.strip('.')

print(format_ip(1))
print(format_ip(256))
print(format_ip(65535))
print(format_ip(777))
