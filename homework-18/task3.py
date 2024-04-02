from typing import Iterable

def y_zip(itr1, itr2):
    if not (isinstance(itr1, Iterable) and isinstance(itr2, Iterable)):
        raise TypeError('Input must be an iterable')

    iterator1 = iter(itr1)
    iterator2 = iter(itr2)

    while True:
        item1 = next(iterator1, None)
        item2 = next(iterator2, None)

        if item1 is None or item2 is None:
            break

        yield item1, item2

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
zipper = y_zip(list1, list2)
print(list(zipper))
