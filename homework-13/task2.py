from array import array


class Matrix:
    def __init__(self, cols, rows, default_value=0, typecode='l'):
        self.cols = cols
        self.rows = rows

        valid_types = set('bBuhHiIlLqQfd')
        if typecode not in valid_types:
            raise ValueError(f'Invalid typecode "{typecode}".')

        self.matrix = array('b', [default_value] * (cols * rows))

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


m = Matrix(11, 5, 8, typecode='b')
print(m)
