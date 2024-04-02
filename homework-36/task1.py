from array import array


class Matrix:
    def __init__(self, data, cols, rows=None, default_value=0, dtype='b'):
        if rows is None:
            rows = len(data) // cols

        self.cols = cols
        self.rows = rows
        self.default_value = default_value
        self.dtype = dtype

        self.matrix = array(self.dtype, data)

    def set(self, x, y, value):
        if not (0 <= x < self.cols and 0 <= y < self.rows):
            raise IndexError('Index out of range')

        index = y * self.cols + x
        self.matrix[index] = value

    def get(self, x, y):
        if not (0 <= x < self.cols and 0 <= y < self.rows):
            raise IndexError('Index out of range')

        index = y * self.cols + x
        return self.matrix[index]

    def __getitem__(self, key):
        if isinstance(key, int):
            x = key % self.cols
            y = key // self.cols
            return self.get(x, y)
        elif isinstance(key, slice):
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else self.cols * self.rows
            step = key.step if key.step is not None else 1

            lst = [self.matrix[i] for i in range(start, stop, step)]
            return Matrix(lst, 1, len(lst), default_value=self.default_value, dtype=self.dtype)
        else:
            raise TypeError('Unsupported index type')

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else self.cols * self.rows
            step = key.step if key.step is not None else 1

            indices = range(start, stop, step)

            value = [value] * len(indices)

            for index, val in zip(indices, value):
                self.matrix[index] = val
        else:
            raise TypeError('Unsupported index type')

    def _apply_operation(self, other, operation):
        if isinstance(other, Matrix):
            if self.cols == other.cols and self.rows == other.rows:
                result_data = [operation(x, y) for x, y in zip(self.matrix, other.matrix)]
                return Matrix(result_data, self.cols, self.rows, self.default_value, self.dtype)
            else:
                raise ValueError('Matrices must have the same dimensions for the operation.')
        else:
            result_data = [operation(x, other) for x in self.matrix]
            return Matrix(result_data, self.cols, self.rows, self.default_value, self.dtype)

    def __add__(self, other):
        return self._apply_operation(other, operation=lambda x, y: x + y)

    def __sub__(self, other):
        return self._apply_operation(other, operation=lambda x, y: x - y)

    def __mul__(self, other):
        return self._apply_operation(other, operation=lambda x, y: x * y)

    def __truediv__(self, other):
        return self._apply_operation(other, operation=lambda x, y: int(x / y))

    def shape(self, new_cols, new_rows):
        if new_cols * new_rows != len(self.matrix):
            raise ValueError('New shape must have the same number of elements as the original matrix')

        return Matrix(self.matrix, new_cols, new_rows, self.default_value, self.dtype)

    def __str__(self):
        return str(self.matrix)


m = Matrix([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 2)
print(m)
print(m[3])
print(m[2:4])

m[2:5] = 0
print(m)

m1 = Matrix([5, 7, 9], 3, 1)
print(m1 + 3)
print(m1 - 1)
print(m1 * 2)
print(m1 / 2)

m2 = Matrix([0, 1, 2, 3], 4, 1)
print(m2.shape(2, 2))

m3 = Matrix([1, 2, 3, 4], 2, 2)
m4 = Matrix([5, 6, 7, 8], 2, 2)

print(m3 + m4)
print(m3 - m4)
print(m3 * m4)
print(m4 / m3)
