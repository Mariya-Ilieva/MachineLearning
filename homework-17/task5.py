from functools import reduce

def my_reduce(func, iterable, initial=None):
    if initial is None:
        return reduce(func, iterable)

    return reduce(func, iterable, initial)

input_str = 'Hello, Wwoorrlldd!'
char_count = my_reduce(lambda count, char: {**count, char: count.get(char, 0) + 1}, input_str, {})
print(char_count)
