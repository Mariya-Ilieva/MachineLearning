from array import array

class MyArray(array):
    def __setitem__(self, idx, to_insert):
        if not isinstance(to_insert, array):
            raise TypeError('Value to insert must be an array.')

        if isinstance(idx, slice):
            start, stop = idx.start, idx.stop

            if start is None:
                start = 0
            if stop is None:
                stop = len(self)

            start = max(start, 0)
            stop = min(stop, len(self))

            new_elements = array(self.typecode, to_insert)
            del self[start:stop]

            arr = array(self.typecode, self)
            arr[start:start] = new_elements
            super().__setitem__(slice(None), arr)

        else:
            super(MyArray, self).__setitem__(idx, to_insert)

a = MyArray('i', [1, 2, 3, 4])
a[1:2] = array('i', [7, 8, 9])
print(a)
# a[2:3] = array('i', [11, 101, 1300])
# print(a)
