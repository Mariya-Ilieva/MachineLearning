import re


p1 = r'ca[rt]'
p2 = r'pr?op'
p3 = r'ferr(et|y|ari)'
p4 = r'\w*ious\b'
p5 = r'\s[.,:;]'
p6 = r'\w{7,}'
p7 = r'\b[^eE\W]+\b'

s1 = ['my car', 'bad cats', 'camper', 'high art']
s2 = ['pop culture', 'mad props', 'plop', 'prrrop']
s3 = ['ferret', 'ferry', 'ferrari', 'ferrum', 'transfer A']
s4 = ['how delicious', 'spacious room', 'ruinous', 'consciousness']
s5 = ['bad punctuation .', 'escape the period']
s6 = ['Siebentausenddreihundertzweiundzwanzig', 'no', 'three small words']
s7 = ['red platypus', 'wobbling nest', 'earth bed', 'bedrøvet abe', 'BEET']

for s in s1:
    print(bool(re.search(p1, s)))
print('\n')

for s in s2:
    print(bool(re.search(p2, s)))
print('\n')

for s in s3:
    print(bool(re.search(p3, s)))
print('\n')

for s in s4:
    print(bool(re.search(p4, s)))
print('\n')

for s in s5:
    print(bool(re.search(p5, s)))
print('\n')

for s in s6:
    print(bool(re.search(p6, s)))
print('\n')

for s in s7:
    print(bool(re.search(p7, s)))
print('\n')
