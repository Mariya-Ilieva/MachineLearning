import re


def convert_currency_in_text(text, dict_rates, symbol):
    for currency, rate in dict_rates.items():
        pattern = rf'({re.escape(currency)}|\$|€|£|¥|USD|CHF|RON|GBP)(\s*[0-9]+(?:\.[0-9]{2})?)'
        replacement = lambda match: f'{float(match.group(2).replace(",", "")) * rate:.2f} {symbol}'
        text = re.sub(pattern, replacement, text)

    return text


exchange_rates = {'USD': 1.80277, 'BGN': 1.00000, 'CHF': 2.03541, 'RON': 3.93385, 'EUR': 1.95583, 'GBP': 2.28637}

text1 = 'Price: $25.00, valid today only'
print(convert_currency_in_text(text1, exchange_rates, 'BGN'))

text2 = 'Ivan Petrov: salary 2000 € for March 2024'
print(convert_currency_in_text(text2, exchange_rates, 'BGN'))
