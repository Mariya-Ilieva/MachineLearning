from typing import Iterable
import types

def my_reduce(func, iterable, initial=None):
    if not isinstance(iterable, Iterable):
        raise TypeError(f'{type(iterable)} must be an iterable')

    if not isinstance(func, types.FunctionType):
        raise TypeError(f'{func} should be a function')

    iterator = iter(iterable)

    if initial is None:
        res = next(iterator)
    else:
        res = initial

    for element in iterator:
        res = func(res, element)

    return res

my_list = [1, 2, 3, 4, 5, 6]
result = my_reduce(lambda x, y: x + y, my_list) / len(my_list)
print(result)
