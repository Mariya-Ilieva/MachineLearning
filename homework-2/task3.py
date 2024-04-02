alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_letters(letters, n):
    output = ''
    alphabet_len = len(alphabet)

    for letter in letters:
        new_index = alphabet.index(letter) + n
        if new_index > alphabet_len:
            new_index -= alphabet_len
        output += alphabet[new_index]

    return output

print(encrypt_letters('abc', 1))
print(encrypt_letters('abc', 3))
print(encrypt_letters('zab', 2))
print(encrypt_letters('machinelearning', 4))
