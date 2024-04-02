def convert_ip(ip):
    groups = ip.split('.')

    result = 0
    for i in range(4):
        result = (result << 8) + int(groups[i])

    return result

print(convert_ip('255.255.255.255'))
print(convert_ip('0.0.0.1'))
print(convert_ip('0.0.1.1'))
print(convert_ip('255.168.98.3'))
