def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_between(date1, date2):
    d1, m1, y1 = map(int, date1.split('-'))
    d2, m2, y2 = map(int, date2.split('-'))
    year = [31, 28 + leap_year(y1), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if y1 == y2:

        if m1 == m2:
            return d2 - d1

        else:
            days_month = 31 - d1
            days_months = sum(year[m1:m2-1])
            return days_month + days_months + d2

    else:
        days_year1 = sum(year[m1-1:]) - d1
        days_year2 = sum(year[:m2-1]) + d2
        days_between_years = (y2 - y1 - 1) * 365 + sum([leap_year(y) for y in range(y1 + 1, y2)])
        return days_year1 + days_year2 + days_between_years

print(days_between('11-06-2021', '12-06-2021'))
print(days_between('1-01-2021', '1-02-2021'))
print(days_between('22-01-2023', '22-01-2024'))
