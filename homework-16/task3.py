brackets = {'(': ')', '{': '}', '[': ']'}
open_brackets = brackets.keys()
closing_brackets = brackets.values()

def valid_brackets(s):
    output = []

    for br in s:
        if br in open_brackets:
            output.append(br)
        elif br in closing_brackets:
            if not output or brackets[output.pop()] != br:
                return False

    return len(output) == 0

print(valid_brackets('((101))'))
print(valid_brackets('()[M]{}'))
print(valid_brackets('(]'))
print(valid_brackets('([)]'))
print(valid_brackets('{[];;}'))
