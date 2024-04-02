def split_lines(s):
    s = s.strip()
    l = len(s)
    start = 0
    temp = 0

    while temp < l:
        if s[temp] == '\n':
            yield s[start:temp]
            start = temp + 1

        temp += 1

    if start < temp:
        yield s[start:temp]

s = '''
ala
bala
portokala

Mimi
'''

lines = split_lines(s)
for line in lines:
  print(line)
