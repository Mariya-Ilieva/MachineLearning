class MyZip:
    def __init__(self, *itrs):
        self.iterators = [iter(i) for i in itrs]

    def __iter__(self):
        return self

    def __next__(self):
        result = tuple(next(i, None) for i in self.iterators)

        if None in result:
            raise StopIteration

        return result


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
zipper = MyZip(list1, list2)
print(list(zipper))
