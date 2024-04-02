class MyCounter:
    def __init__(self, iterable=None, **kwargs):
        self.counter = {}

        if iterable:
            if not hasattr(iterable, '__iter__'):
                raise TypeError(f'Invalid input {iterable}. Input must be iterable.')
            self.update(iterable)

        elif kwargs:
            self.update(kwargs)

    def update(self, iterable):
        if isinstance(iterable, dict):
            for el, count in iterable.items():
                self.counter[el] = self.counter.get(el, 0) + count
        else:
            for el in iterable:
                self.counter[el] = self.counter.get(el, 0) + 1

    def __repr__(self):
        return repr(self.counter)


print(MyCounter())
print(MyCounter('gallahad'))
print(MyCounter({'red': 4, 'blue': 2}))
print(MyCounter(cats=4, dogs=8))
