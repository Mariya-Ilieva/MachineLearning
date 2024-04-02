class MyEnumerate:
    def __init__(self, itr, start=0):
        self.itr = itr
        self.start = start
        self.idx = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1

        if self.idx >= len(self.itr):
            raise StopIteration

        return self.idx, self.itr[self.idx]


my_list = ['a', 'b', 'c', 'd', 'e']
enumerator = MyEnumerate(my_list)
print(list(enumerator))
