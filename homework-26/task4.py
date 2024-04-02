from datetime import datetime

# def format_date(date, format_string):
#     if not isinstance(date, (datetime, date)):
#         raise ValueError(f'The {date} parameter should be a datetime or date object.')
#
#     placeholders = {
#         '%Y': str(date.year),
#         '%m': str(date.month).zfill(2),
#         '%d': str(date.day).zfill(2),
#         '%H': str(date.hour).zfill(2),
#         '%M': str(date.minute).zfill(2),
#         '%S': str(date.second).zfill(2),
#         '%A': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][date.weekday()],
#         '%B': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
#                'November', 'December'][date.month - 1]
#     }
#
#     output = format_string
#     for p, v in placeholders.items():
#         output = output.replace(p, v)
#
#     return output
#
# date_obj = datetime(2012, 9, 23, 21, 37, 4, 177393)
# formatted_string = format_date(date_obj, '%A %B %d, %Y %H:%M:%S')
# print(formatted_string)

def get_placeholder_value(date, placeholder):
    if placeholder == '%Y':
        return str(date.year)

    elif placeholder == '%m':
        return str(date.month).zfill(2)

    elif placeholder == '%d':
        return str(date.day).zfill(2)

    elif placeholder == '%H':
        return str(date.hour).zfill(2)

    elif placeholder == '%M':
        return str(date.minute).zfill(2)

    elif placeholder == '%S':
        return str(date.second).zfill(2)

    elif placeholder == '%A':
        return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][date.weekday()]

    elif placeholder == '%B':
        return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December'][date.month - 1]

    else:
        return placeholder

def format_date(date, format_string):
    if not isinstance(date, (datetime, date)):
        raise ValueError(f'The {date} parameter should be a datetime or date object.')

    output = ''
    i = 0

    while i < len(format_string):
        if format_string[i] == '%':
            placeholder = format_string[i:i + 2]
            output += get_placeholder_value(date, placeholder)
            i += 2
        else:
            output += format_string[i]
            i += 1

    return output

date_obj = datetime(2012, 9, 23, 21, 37, 4, 177393)
formatted_string = format_date(date_obj, '%A %B %d, %Y %H:%M:%S')
print(formatted_string)
