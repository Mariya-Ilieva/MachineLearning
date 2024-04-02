from typing import Iterable
import types

def my_filter(func, iterable):
    if not isinstance(iterable, Iterable):
        raise TypeError(f'{type(iterable)} must be an iterable')

    if not isinstance(func, types.FunctionType):
        raise TypeError(f'{func} should be a function')

    return [x for x in iterable if func(x)]

result = my_filter(lambda x: isinstance(x, int), ['me', 1, 2, 3, 'o', 4, 5, 6])
print(result)

result = my_filter(lambda x: x > 0, [1, 2, 3, -6, -11, 4, 5, 6])
print(result)
