import re


class MyDate:
    def __init__(self, year, month, day, hour, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f'{self.year}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}'


def my_strptime(date, output):
    pattern = output.replace('%Y', r'(?P<year>\d{4})') \
                    .replace('%m', r'(?P<month>\d{2})') \
                    .replace('%d', r'(?P<day>\d{2})') \
                    .replace('%H', r'(?P<hour>\d{2})') \
                    .replace('%M', r'(?P<minute>\d{2})')

    match = re.match(pattern, date)

    if match:
        month = int(match.group('month'))

        if not 12 >= month >= 1:
            raise ValueError('Month must be in the range 1 to 12')

        values = [int(value) for value in match.groups()]

        return MyDate(*values)

result = my_strptime('2020-01-01 14:00', '%Y-%m-%d %H:%M')
print(result)
