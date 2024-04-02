def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def leap_years_count(y1, y2):
    c = 0

    for y in range(y1, y2 + 1):
        if is_leap(y):
            c += 1

    return f'Count of leap years between {y1} and {y2} is {c}'

year1 = 2021
year2 = 2024
print(leap_years_count(year1, year2))

year3 = 2010
year4 = 2020
print(leap_years_count(year3, year4))
