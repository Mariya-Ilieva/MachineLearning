def non_repeating_letter_idx(s):
    l_count = [s.count(l) for l in s]

    idx = -1
    for i, j in enumerate(l_count):
        if j == 1:
            idx = i
            break

    return idx

print(non_repeating_letter_idx('alabala'))
print(non_repeating_letter_idx('github'))
print(non_repeating_letter_idx('alabalab'))
print(non_repeating_letter_idx('MimimimimiMimiprrrrrrrrrrrrrr'))
