def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    days_per_month = [31, 28 + leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_per_month[month - 1]

def days_between(date1, date2):
    d1, m1, y1 = map(int, date1.split('-'))
    d2, m2, y2 = map(int, date2.split('-'))

    def days_in_year(month, day, year):
        return sum(days_in_month(m, year) for m in range(month, 13)) - day

    days_year1 = days_in_year(m1, d1, y1)
    days_year2 = sum(days_in_month(m, y2) for m in range(1, m2)) + d2
    days_between_years = (y2 - y1 - 1) * 365 + sum(leap_year(y) for y in range(y1 + 1, y2))

    return days_year1 + days_year2 + days_between_years

print(days_between('11-06-2021', '12-06-2021'))
print(days_between('1-01-2021', '1-02-2021'))
print(days_between('22-01-2023', '22-01-2024'))
