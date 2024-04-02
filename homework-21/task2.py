from array import array
from random import randint


class Matrix:
    def __init__(self, cols, rows, *, fill=None, default_value=0, dtype='b'):
        self.cols = cols
        self.rows = rows
        self.default_value = default_value
        self.dtype = dtype

        list = [fill(x, y) for y in range(rows) for x in range(cols)] if fill else \
               [default_value] * (rows * cols)

        self.matrix = array(self.dtype, list)

    def set(self, x, y, value):
        if not (0 <= x < self.cols and 0 <= y < self.rows):
            raise IndexError

        index = y * self.cols + x
        self.matrix[index] = value

    def get(self, x, y):
        if not (0 <= x < self.cols and 0 <= y < self.rows):
            raise IndexError

        index = y * self.cols + x
        return self.matrix[index]

    def __str__(self):
        return str(self.matrix)


m = Matrix(2, 3, default_value=8, dtype=' ')
print(m)

m1 = Matrix(2, 3, fill=lambda x, y: randint(0, 10))
print(m1)
