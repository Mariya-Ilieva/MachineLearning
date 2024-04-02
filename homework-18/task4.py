from typing import Iterable

def y_enumerate(itr, start=0):
    if not isinstance(itr, Iterable):
        raise TypeError(f'{type(itr)} must be an iterable')

    iterator = iter(itr)
    index = start

    while True:
        item = next(iterator, None)

        if item is None:
            break

        yield index, item
        index += 1

letters = ['a', 'b', 'c']
enumerated = y_enumerate(letters, start=1)
print(list(enumerated))
