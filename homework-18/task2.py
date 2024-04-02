from typing import Iterable
import types

def y_filter(func, itr):
    if not isinstance(itr, Iterable):
        raise TypeError(f'{type(itr)} must be an iterable')

    if not isinstance(func, types.FunctionType):
        raise TypeError(f'{func} should be a function')

    for x in itr:
        if func(x):
            yield x

result = y_filter(lambda x: isinstance(x, int), ['me', 1, 2, 3, 'o', 4, 5, 6])
print(list(result))

result = y_filter(lambda x: x > 0, [1, 2, 3, -6, -11, 4, 5, 6])
print(list(result))
