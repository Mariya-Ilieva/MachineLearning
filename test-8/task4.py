MONTHS_31 = [1, 3, 5, 7, 8, 10, 12]
MONTHS_30 = [4, 6, 9, 11]

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def valid_date(s):
    parts = s.split('-')

    if len(parts) != 3:
        return False

    d, m, y = map(int, parts)

    if d < 1 or m < 1 or m > 12:
        return False

    if m in MONTHS_31:
        return 1 <= d <= 31
    elif m in MONTHS_30:
        return 1 <= d <= 30
    elif m == 2:
        return 1 <= d <= 28 if not is_leap(y) else 1 <= d <= 29

    return False

print(valid_date('12-12-2012'))
print(valid_date('30-02-2012'))
print(valid_date('1-1-2012'))
