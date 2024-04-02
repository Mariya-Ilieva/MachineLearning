class Llist(list):
    def __init__(self, l):
        super().__init__()

        self.l = l

    def __getitem__(self, sl):
        if not isinstance(sl, slice):
            raise TypeError(f'{type(slice)} must be a slice')

        start = sl.start
        end = sl.stop

        if start is None:
            start = 0

        if end is None:
            end = 0

        return self.lazy_slice(start, end)

    def lazy_slice(self, start, end):
        idx = start

        while idx < end:
            yield self.l[idx]
            idx += 1

x = Llist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ex = x[2:8]

for el in ex:
    print(el, end=', ')
