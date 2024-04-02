import re


# def convert_date_format_eu(american):
#     match = re.match(r'(\d{2})/(\d{2})/(\d{4})', american)
#
#     if match:
#         m, d, y = map(int, match.groups())
#         european = f'{d:02d}.{m:02d}.{y}'
#         return european
#
#     else:
#         return 'Invalid date format'

def convert_date_format_eu(american):
    european = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2.\1.\3', american)
    return european

ads = '05/01/2024'
eds = convert_date_format_eu(ads)
print(eds)

ads = '08/22/2000'
eds = convert_date_format_eu(ads)
print(eds)
