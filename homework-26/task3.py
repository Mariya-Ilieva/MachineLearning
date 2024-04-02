from datetime import datetime, timedelta
from pytz import timezone
import calendar


# да се покаже текущото време в Париж
paris_tz = timezone('Europe/Paris')
paris_time = datetime.now(paris_tz)
paris_time_str = paris_time.strftime('%Y-%m-%d %H:%M:%S')
print('The time in Paris now is:', paris_time_str)


# от зададена дата и час местно време в София да се покаже местното време и час в Берлин
sofia_tz = timezone('Europe/Sofia')
sofia_time = datetime.now()
berlin_tz = timezone('Europe/Berlin')
berlin_time = sofia_time.astimezone(berlin_tz)
berlin_time_str = berlin_time.strftime('%Y-%m-%d %H:%M:%S %Z')
print('The time in Berlin now is:', berlin_time_str)


# при зададена дата да покаже следващата
current_date = datetime.now()
next_date = current_date + timedelta(days=1)
next_date_str = next_date.strftime('%Y-%m-%d')
print('Next date is:', next_date_str)


# при зададена дата да даде датата на понеделник от същата седмица
current_date = datetime.now()
mon_date = current_date - timedelta(days=current_date.weekday())
mon_date_str = mon_date.strftime('%Y-%m-%d')
print('Monday this week was:', mon_date_str)


# при зададена дата да върне датата на следващия петък
current_date = datetime.now()
fri_date = current_date + timedelta(days=(4 - current_date.weekday() + 7) % 7)
fri_date_str = fri_date.strftime('%Y-%m-%d')
print('Next friday will be:', fri_date_str)


# при дадена дата да върне последния петък от месеца
current_date = datetime.now()
year = current_date.year
month = current_date.month
last_day_month = calendar.monthrange(year, month)[1]
days_until_last_friday = (calendar.weekday(year, month, last_day_month) - calendar.FRIDAY) % 7
last_friday = datetime(year, month, last_day_month) - timedelta(days=days_until_last_friday)
# last_day_month = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
# days_until_last_friday = (last_day_month.weekday() - 4) % 7
# last_friday = last_day_month - timedelta(days=days_until_last_friday)
last_friday_str = last_friday.strftime('%Y-%m-%d')
print('Last Friday of this month is: ', last_friday_str)


# функция която връща итератор за всички дати от съответния месец като стрингове
def date_range(year, month):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) - timedelta(days=1)

    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime('%Y-%m-%d')
        current_date += timedelta(days=1)

for date_str in date_range(2024, 2):
    print(date_str)
