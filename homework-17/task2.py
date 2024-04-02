from typing import Iterable
import types

def my_map(func, iterable):
    if not isinstance(iterable, Iterable):
        raise TypeError(f'{type(iterable)} must be an iterable')

    if not isinstance(func, types.FunctionType):
        raise TypeError(f'{func} should be a function')

    return [func(x) for x in iterable]

result = my_map(lambda x: x*x, [1, 2, 3, 4])
print(result)
