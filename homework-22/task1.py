from array import array


class SymmetricMatrix:
    def __init__(self, size, default=0, typecode='b'):
        if size <= 0:
            raise ValueError('Invalid size given.')

        self.size = size
        self.default = default
        self.typecode = typecode
        self.matrix = [array(self.typecode, [default] * (i + 1)) for i in range(size)]

    @staticmethod
    def change_index(r, c):
        if r < c:
            return c, r

        return r, c

    def _valid_index(self, idx):
        row, col = idx

        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            raise IndexError('Index out of range.')

    def __setitem__(self, idx, val):
        self._valid_index(idx)

        row, col = idx
        row, col = self.change_index(row, col)

        self.matrix[row][col] = val

    def __getitem__(self, idx):
        self._valid_index(idx)

        row, col = idx
        row, col = self.change_index(row, col)

        return self.matrix[row][col]

    def __str__(self):
        return str(self.matrix)


sm = SymmetricMatrix(5, 1)
print(sm)

sm[1, 3] = 0
print(sm[3, 1])
