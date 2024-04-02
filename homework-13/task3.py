class ExchangeRate:
    @staticmethod
    def split_function_name(func_name):
        parts = func_name.split('_')

        return parts

    def __init__(self, rate):
        if isinstance(rate, dict):
            self.rate = rate
        elif isinstance(rate, list):
            self.rate = dict(rate)
        else:
            raise ValueError('Invalid input format. Only dictionary or a list of tuples accepted.')

    def __getattr__(self, name):
        if name not in self.rate:
            raise AttributeError(f'There is no currency "{name}" in the exchange')

        return self.rate[name]

    def __setattr__(self, name, value):
        if name == 'rate':
            super().__setattr__(name, value)
        elif name not in self.rate:
            raise AttributeError(f'There is no currency "{name}')
        else:
            self.rate[name] = value

    def change_rate(self, currency, new_rate):
        if currency not in self.rate:
            raise ValueError(f'Invalid currency "{currency}".')

        self.rate[currency] = new_rate

    def change_lv_usd(self, amount):
        parts = self.split_function_name('change_lv_usd')

        if len(parts) != 3:
            raise ValueError('Invalid function name format.')

        xx, yy = parts[1], parts[2]

        if xx not in self.rate or yy not in self.rate:
            raise ValueError('Invalid currency.')

        if xx == yy:
            return amount

        return f'{amount * self.rate[yy] / self.rate[xx]:.3f}'


rates_dict = {'usd': 1.75, 'euro': 1.95, 'gbp': 2.9, 'lv': 1}
rates = ExchangeRate(rates_dict)
print(rates.usd)

price_lv = rates.change_lv_usd(1.5)
print(price_lv)

rates.usd = 1.99
print(rates.usd)
