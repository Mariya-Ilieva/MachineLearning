from array import array


class SymmetricMatrix:
    def __init__(self, size, default=0, typecode='b'):
        if size <= 0:
            raise ValueError('Invalid size given.')

        self.size = size
        self.default = default
        self.typecode = typecode
        self.matrix = [array(self.typecode, [default] * size) for _ in range(size)]

    def __setitem__(self, idx, val):
        row, col = idx

        if row >= self.size or col >= self.size:
            raise ValueError('Index out of range.')

        self.matrix[row][col] = val
        self.matrix[col][row] = val

    def __getitem__(self, idx):
        row, col = idx

        if row >= self.size or col >= self.size:
            raise ValueError('Index out of range.')

        return self.matrix[row][col]

    def __str__(self):
        return str(self.matrix)


sm = SymmetricMatrix(5, 1)
print(sm)

sm[1, 3] = 0
print(sm[3, 1])
