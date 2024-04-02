days_in_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

def day_of_week(date):
    if not all(x.isdigit() for x in date.split('-')):
        raise ValueError(f'Not a valid date: {date}')

    day, month, year = [int(x) for x in date.split('-')]
    days_till_date = days_in_month[month - 1] + day

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and month > 2):
        days_till_date += 1

    leap_years = (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    week_day = days_till_date + (year - 1) + leap_years

    return week_day % 7

print(day_of_week('30-11-2021'))
