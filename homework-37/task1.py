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

    @classmethod
    def arange(cls, start, stop, step=1, dtype='b'):
        data = list(range(start, stop, step))
        return cls(data, len(data), default_value=0, dtype=dtype)

    @classmethod
    def zeros(cls, cols, rows, dtype='b'):
        data = [0] * (cols * rows)
        return cls(data, cols, rows, default_value=0, dtype=dtype)

    @classmethod
    def zeros_like(cls, matrix):
        return cls.zeros(matrix.cols, matrix.rows, dtype=matrix.dtype)

    @classmethod
    def full(cls, shape, fill_value, dtype='b'):
        data = [fill_value] * (shape[0] * shape[1])
        return cls(data, shape[0], shape[1], default_value=0, dtype=dtype)

    def __lt__(self, scalar):
        return Matrix([x < scalar for x in self.matrix], self.cols, self.rows, self.default_value, dtype='b')

    def __le__(self, scalar):
        return Matrix([x <= scalar for x in self.matrix], self.cols, self.rows, self.default_value, dtype='b')

    def __eq__(self, scalar):
        return Matrix([x == scalar for x in self.matrix], self.cols, self.rows, self.default_value, dtype='b')

    def __ne__(self, scalar):
        return Matrix([x != scalar for x in self.matrix], self.cols, self.rows, self.default_value, dtype='b')

    def __gt__(self, scalar):
        return Matrix([x > scalar for x in self.matrix], self.cols, self.rows, self.default_value, dtype='b')

    def __ge__(self, scalar):
        return Matrix([x >= scalar for x in self.matrix], self.cols, self.rows, self.default_value, dtype='b')

    def _process_slice(self, key):
        start = key.start if key.start is not None else 0
        stop = key.stop if key.stop is not None else self.cols * self.rows
        step = key.step if key.step is not None else 1

        return range(start, stop, step)

    def __getitem__(self, key):
        if isinstance(key, int):
            x = key % self.cols
            y = key // self.cols
            return self.get(x, y)
        elif isinstance(key, slice):
            indices = self._process_slice(key)
            lst = [self.matrix[i] for i in indices]
            return Matrix(lst, 1, len(lst), default_value=self.default_value, dtype=self.dtype)
        else:
            raise TypeError('Unsupported index type')

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            indices = self._process_slice(key)
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

    def std(self, axis=None):
        if axis not in (0, 1, None):
            raise ValueError('Invalid axis. Use 0, 1, or None.')

        if axis is None:
            mean_value = sum(self.matrix) / len(self.matrix)
            squared_diff = [(x - mean_value) ** 2 for x in self.matrix]
            variance = sum(squared_diff) / len(self.matrix)
            std_deviation = variance ** 0.5

            return std_deviation
        else:
            if axis == 0:
                values = [self.get(x, y) for y in range(self.rows) for x in range(self.cols)]
            else:  # axis == 1
                values = [self.get(x, y) for x in range(self.cols) for y in range(self.rows)]

            mean_values = [sum(values[i:len(self.matrix)]) / len(self.matrix) for i in range(len(self.matrix))]
            squared_diff = [(values[i] - mean_values[i % len(mean_values)]) ** 2 for i in range(len(values))]
            variance = sum(squared_diff) / len(values)
            std_deviation = variance ** 0.5

            return std_deviation

    def fancy_indexing(self, indices):
        if not isinstance(indices, list):
            raise TypeError('Indices must be provided as a list.')

        result_data = [self.matrix[i] for i in indices]
        return Matrix(result_data, 1, len(result_data), default_value=self.default_value, dtype=self.dtype)

    def __str__(self):
        return str(self.matrix)


m = Matrix([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 2)
m_arange = Matrix.arange(0, 10, 2)
print(m_arange)
m_zeros = Matrix.zeros(3, 2)
print(m_zeros)
m_zeros_like = Matrix.zeros_like(m)
print(m_zeros_like)
m_full = Matrix.full((2, 3), fill_value=5)
print(m_full)

m = Matrix([-1, -3, 0, 1, 2], 2, 3)
bm = m > 0
print(bm)

m = Matrix([1, 2, 3, 4], 2, 2)
print(m.std())
print(m.std(axis=0))
print(m.std(axis=1))

m = Matrix([0, 1, 2, 3, 4, 5, 6, 7], 4, 2)
print(m)
indices1 = [4, 3, 0, 6]
result1 = m.fancy_indexing(indices1)
print(result1)
indices2 = [1, 5, 7, 2, 0, 3]
result2 = m.fancy_indexing(indices2)
print(result2)
