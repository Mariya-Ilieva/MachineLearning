def y_zip(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    i = 0
    j = 0

    while True:
        temp_i = i % len1
        temp_j = j % len2

        el1 = seq1[temp_i]
        el2 = seq2[temp_j]

        yield el1, el2

        i += 1
        j += 1

        if i % len1 == 0 and j % len2 == 0:
            break

s1 = 'Mimimimimimimimimimimimimimimimimi'
s2 = [1, 2]

for e in y_zip(s1, s2):
    print(e)
