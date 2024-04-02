def enough_present(s):
    max_absent = 2
    late = 0
    cons_late = 0

    for i in s:
        if i == 'О':
            max_absent -= 1
            late = 0
        elif i == 'З':
            late += 1
            cons_late = max(late, cons_late)
        elif i == 'П':
            late = 0

        if max_absent < 0 or cons_late >= 3:
            return False

    return True

print(enough_present('ППОЗЗПЗ'))
print(enough_present('ППОЗЗЗ'))
print(enough_present('ППОЗЗОПО'))
print(enough_present('ППОЗЗОП'))
