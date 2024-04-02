class MyCounter:
    def __init__(self, iterable):
        try:
            iter(iterable)
        except TypeError:
            raise TypeError(f'Invalid input {iterable}. Input must be iterable.')

        self.counter_dict = {}
        self.update(iterable)

    def update(self, iterable):
        for el in iterable:
            self[el] += 1

    def __getitem__(self, key):
        return self.counter_dict.get(key, 0)

    def __setitem__(self, key, value):
        self.counter_dict[key] = value

    def __repr__(self):
        return f'MyCounter({self.counter_dict})'


print(MyCounter('Hello from Infinno'))
c = MyCounter(['x','y','z','x','x','x','y', 'z'])
print(c)
print(c['z'])
