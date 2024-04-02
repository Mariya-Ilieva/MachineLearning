def set_bit(num, index):
    mask = 1 << index
    result = num | mask

    return result

def clear_bit(num, index):
    mask = ~(1 << index)
    result = num & mask

    return result

def toggle_bit(num, index):
    mask = 1 << index
    result = num ^ mask

    return result

def get_bit(num, index):
    mask = 1 << index
    result = num & mask

    return result == 1

print(set_bit(1, 1))
print(set_bit(0, 2))

print(clear_bit(3, 0))
print(clear_bit(7, 1))

print(toggle_bit(0, 1))
print(toggle_bit(5, 0))

print(get_bit(5, 0))
print(get_bit(4, 0))
