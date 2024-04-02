def manipulate_string(instr):
    output = []

    for ch in instr:
        if ch == '#':
            if output:
                output.pop()
        else:
            output.append(ch)

    return ''.join(output)

print(manipulate_string('abc#'))
print(manipulate_string('a#bc'))
print(manipulate_string('abc##'))
print(manipulate_string('a##bc'))
