from typing import Iterable
import types

def y_map(func, itr):
    if not isinstance(itr, Iterable):
        raise TypeError(f'{type(itr)} must be an iterable')

    if not isinstance(func, types.FunctionType):
        raise TypeError(f'{func} should be a function')

    for x in itr:
        yield func(x)

result = y_map(lambda x: x*x, [1, 2, 3, 4])
print(list(result))
