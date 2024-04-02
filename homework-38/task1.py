class Matrix:
    def __init__(self, data, rows, cols, default_value=0, dtype='b'):
        if rows * cols != len(data):
            raise ValueError('Data size does not match the given dimensions.')

        self.rows = rows
        self.cols = cols
        self.default_value = default_value
        self.dtype = dtype

        self.buffer = bytearray(data)
        self.matrix = [memoryview(self.buffer)[i * self.cols: (i + 1) * self.cols] for i in range(self.rows)]

    def set(self, row, col, value):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError('Index out of range')

        self.matrix[row][col] = value

    def get(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError('Index out of range')

        return self.matrix[row][col]

    def _process_slice(self, slice, lenght):
        start = slice.start if slice.start is not None else 0
        stop = slice.stop if slice.stop is not None else lenght
        step = slice.step if slice.step is not None else 1

        return start, stop, step

    def __getitem__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            row_slice, col_slice = key

            if isinstance(row_slice, slice):
                row_start, row_stop, row_step = self._process_slice(row_slice, self.rows)
                rows = range(max(0, min(row_start, self.rows)), min(self.rows, max(0, row_stop)), row_step)
            elif isinstance(row_slice, int):
                rows = [min(max(row_slice, 0), self.rows - 1)]
            else:
                raise TypeError('Row index must be a slice or an integer')

            if isinstance(col_slice, slice):
                col_start, col_stop, col_step = self._process_slice(col_slice, self.cols)
                cols = range(max(0, min(col_start, self.cols)), min(self.cols, max(0, col_stop)), col_step)
            elif isinstance(col_slice, int):
                cols = [min(max(col_slice, 0), self.cols - 1)]
            else:
                raise TypeError('Column index must be a slice or an integer')

            data = [self.get(x, y) for y in rows for x in cols]
            return Matrix(data, len(cols), len(rows), default_value=self.default_value, dtype=self.dtype)

        elif isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            if step is None:
                step = 1

            if not isinstance(step, int) or step <= 0:
                raise ValueError('Step must be a positive integer')

            if isinstance(key, slice):
                row_start, row_stop, _ = self._process_slice(key, self.rows)
                rows = range(max(0, min(row_start, self.rows)), min(self.rows, max(0, row_stop)), step)
            elif isinstance(key, int):
                rows = [min(max(key, 0), self.rows - 1)]
            else:
                raise TypeError('Row index must be a slice or an integer')

            if isinstance(key, slice):
                col_start, col_stop, _ = self._process_slice(key, self.cols)
                cols = range(max(0, min(col_start, self.cols)), min(self.cols, max(0, col_stop)), step)
            elif isinstance(key, int):
                cols = [min(max(key, 0), self.cols - 1)]
            else:
                raise TypeError('Column index must be a slice or an integer')

            data = [self.get(x, y) for y in rows for x in cols]
            return Matrix(data, len(cols), len(rows), default_value=self.default_value, dtype=self.dtype)

        else:
            raise TypeError('Unsupported index type')

    def __setitem__(self, key, value):
        if isinstance(key, tuple) and len(key) == 2:
            row_slice, col_slice = key

            if isinstance(row_slice, slice):
                row_start, row_stop, row_step = self._process_slice(row_slice, self.rows)
                rows = range(max(0, min(row_start, self.rows)), min(self.rows, max(0, row_stop)), row_step)
            elif isinstance(row_slice, int):
                rows = [min(max(row_slice, 0), self.rows - 1)]
            else:
                raise TypeError('Row index must be a slice or an integer')

            if isinstance(col_slice, slice):
                col_start, col_stop, col_step = self._process_slice(col_slice, self.cols)
                cols = range(max(0, min(col_start, self.cols)), min(self.cols, max(0, col_stop)), col_step)
            elif isinstance(col_slice, int):
                cols = [min(max(col_slice, 0), self.cols - 1)]
            else:
                raise TypeError('Column index must be a slice or an integer')

            for y in rows:
                for x in cols:
                    self.set(x, y, value)
        else:
            raise TypeError('Unsupported index type')

    @classmethod
    def arrange(cls, stop, start=0, step=1, dtype='b'):
        data = list(range(start, stop, step))
        return cls(data, 1, len(data), default_value=0, dtype=dtype)

    @classmethod
    def zeros(cls, rows, cols, dtype='b'):
        data = [0] * (rows * cols)
        return cls(data, rows, cols, default_value=0, dtype=dtype)

    @classmethod
    def zeros_like(cls, matrix):
        return cls.zeros(matrix.rows, matrix.cols, dtype=matrix.dtype)

    @classmethod
    def full(cls, shape, fill_value, dtype='b'):
        rows, cols = shape
        data = [fill_value] * (rows * cols)
        return cls(data, rows, cols, default_value=0, dtype=dtype)

    @classmethod
    def meshgrid(cls, m_x, m_y):
        if not isinstance(m_x, Matrix) or not isinstance(m_y, Matrix):
            raise TypeError('Both inputs must be Matrix objects.')

        count_x = m_x.rows
        count_y = m_y.cols

        data_x = m_x.matrix * count_y
        data_y = m_y.matrix * count_x

        mesh_x = cls(data_x.flatten(), m_x.rows, m_y.cols)
        mesh_y = cls(data_y.flatten(), m_x.rows, m_y.cols)

        return mesh_x, mesh_y

    def __lt__(self, scalar):
        return Matrix([x < scalar for x in self.matrix], self.rows, self.cols, default_value=self.default_value,
                      dtype='b')

    def __le__(self, scalar):
        return Matrix([x <= scalar for x in self.matrix], self.rows, self.cols, default_value=self.default_value,
                      dtype='b')

    def __eq__(self, scalar):
        return Matrix([x == scalar for x in self.matrix], self.rows, self.cols, default_value=self.default_value,
                      dtype='b')

    def __ne__(self, scalar):
        return Matrix([x != scalar for x in self.matrix], self.rows, self.cols, default_value=self.default_value,
                      dtype='b')

    def __gt__(self, scalar):
        return Matrix([x > scalar for x in self.matrix], self.rows, self.cols, default_value=self.default_value,
                      dtype='b')

    def __ge__(self, scalar):
        return Matrix([x >= scalar for x in self.matrix], self.rows, self.cols, default_value=self.default_value,
                      dtype='b')

    def _apply_operation(self, other, operation):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                result_data = [operation(x, y) for x, y in zip(self.matrix, other.matrix)]
                return Matrix(result_data, self.rows, self.cols, default_value=self.default_value, dtype=self.dtype)
            else:
                raise ValueError('Matrices must have the same dimensions for the operation.')
        else:
            result_data = [operation(x, other) for x in self.matrix]
            return Matrix(result_data, self.rows, self.cols, default_value=self.default_value, dtype=self.dtype)

    def __add__(self, other):
        return self._apply_operation(other, operation=lambda x, y: x + y)

    def __sub__(self, other):
        return self._apply_operation(other, operation=lambda x, y: x - y)

    def __mul__(self, other):
        return self._apply_operation(other, operation=lambda x, y: x * y)

    def __truediv__(self, other):
        return self._apply_operation(other, operation=lambda x, y: int(x / y))

    def reshape(self, idxs):
        self.rows, self.cols = idxs
        return self.rows, self.cols

    def fancy_indexing(self, indices):
        if not isinstance(indices, list):
            raise TypeError('Indices must be provided as a list.')

        result_data = [self.matrix[i] for i in indices]
        return Matrix(result_data, 1, len(result_data), default_value=self.default_value, dtype=self.dtype)

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
                values = [self.get(i, j) for j in range(self.cols) for i in range(self.rows)]
            else:  # axis == 1
                values = [self.get(i, j) for i in range(self.rows) for j in range(self.cols)]

            mean_values = [sum(values[i:len(self.matrix)]) / len(self.matrix) for i in range(len(self.matrix))]
            squared_diff = [(values[i] - mean_values[i % len(mean_values)]) ** 2 for i in range(len(values))]
            variance = sum(squared_diff) / len(values)
            std_deviation = variance ** 0.5

            return std_deviation

    def dot(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Can only perform dot product with another Matrix object.')

        if self.cols != other.rows:
            raise ValueError(
                'Number of columns in the first matrix must be equal to the number of rows in the second matrix.')

        result_rows = self.rows
        result_cols = other.cols

        for i in range(result_rows):
            for j in range(result_cols):
                prod = 0

                for k in range(self.cols):
                    prod += self.get(i, k) * other.get(k, j)
                self.set(i, j, prod)

        self.cols = result_cols
        return self

    def in1d(self, elements):
        if not isinstance(elements, list):
            raise TypeError('Input elements must be provided as a list.')

        return [el in self.buffer for el in elements]

    def unique(self):
        elements = []

        for row in self.matrix:
            for el in row:
                if el not in elements:
                    elements.append(el)

        return elements

    def intersect1d(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Input must be a Matrix object.')

        return [el for el in self.unique() if el in other.unique()]

    def union1d(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Input must be a Matrix object.')

        return self.unique() + [elem for elem in other.unique() if elem not in self.unique()]

    def sum(self, axis=None):
        if axis is None:
            return sum(self.buffer)

        if axis == 0:
            return [sum(self.matrix[i][j] for i in range(self.rows)) for j in range(self.cols)]

        if axis == 1:
            return [sum(row) for row in self.matrix]

        raise ValueError('Invalid axis. Use 0, 1, or None.')

    def cumsum(self, axis=None):
        if axis is None:
            return [sum(self.buffer[:i + 1]) for i in range(len(self.buffer))]

        if axis == 0:
            return [[sum(self.matrix[i][:j + 1]) for j in range(self.cols)] for i in range(self.rows)]

        if axis == 1:
            return [self.matrix[i][:j+1] for i in range(self.rows) for j in range(self.cols)]

        raise ValueError('Invalid axis. Use 0, 1, or None.')

    def mean(self, axis=None):
        if axis is None:
            return sum(self.buffer) / len(self.buffer)

        if axis == 0:
            return [sum(self.matrix[i]) / self.cols for i in range(self.rows)]

        if axis == 1:
            return [sum(row) / self.cols for row in self.matrix]

        raise ValueError('Invalid axis. Use 0, 1, or None.')

    def vstack(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Input must be a Matrix object.')

        if self.cols != other.cols:
            raise ValueError('Number of columns must match for vertical stacking.')

        data = self.buffer + other.buffer
        return Matrix(data, self.rows + other.rows, self.cols, default_value=self.default_value, dtype=self.dtype)

    def hstack(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Input must be a Matrix object.')

        if self.rows != other.rows:
            raise ValueError('Number of rows must match for horizontal stacking.')

        data = [self.matrix[i] + other.matrix[i] for i in range(self.rows)]
        return Matrix(data, self.rows, self.cols + other.cols, default_value=self.default_value, dtype=self.dtype)

    def split(self, indices, axis=0):
        if axis not in (0, 1):
            raise ValueError('Invalid axis. Use 0 or 1.')

        if axis == 0:
            if isinstance(indices, int):
                indices = [indices]
            indices.append(self.rows)

            result = []
            start = 0
            for end in indices:
                result.append(Matrix(self.buffer[start * self.cols:end * self.cols], end - start, self.cols,
                                              default_value=self.default_value, dtype=self.dtype))
                start = end

            return result

        elif axis == 1:
            if isinstance(indices, int):
                indices = [indices]
            indices.append(self.cols)

            result = []
            for i in range(len(indices) - 1):
                start = indices[i]
                end = indices[i + 1]
                result.append(Matrix([row[start:end] for row in self.matrix], self.rows, end - start,
                                              default_value=self.default_value, dtype=self.dtype))

            return result

    def vsplit(self, indices):
        return self.split(indices, axis=0)

    def hsplit(self, indices):
        return self.split(indices, axis=1)

    def tile(self, reps):
        if isinstance(reps, int):
            reps = (reps, reps)
        elif isinstance(reps, tuple) and len(reps) == 1:
            reps = (reps[0], reps[0])

        data = []
        for _ in range(reps[0]):
            for row in self.matrix:
                data.extend(row * reps[1])

        return Matrix(data, self.rows * reps[0], self.cols * reps[1],
                      default_value=self.default_value, dtype=self.dtype)

    def __str__(self):
        result = ''

        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.get(i, j)) + ' '
            result += '\n'

        return result


# m = Matrix([1, 2, 3, 4, 5, 6], 2, 3)

# print(m[0:2, 3:4])
# print(m[:, 3:4])
# print(m[1:3, 4])
# print(m[0:2, 3])

# m[0:2, 3:4] = 3
# print(m)
# m[:, 3:4] = 1
# print(m)
# m[1:3, 4] = 0
# print(m)
# m[0:2, 3] = 4
# print(m)

# bm = m > 0
# data = Matrix([[4, 7], [0, 2], [-5, 6]], 3, 2)
# print(data[bm])

# m1 = Matrix([[1, 2, 3], [4, 5, 6]], 2, 3)
# m2 = Matrix([[6, 5], [4, 3], [2, 1]], 3, 2)
# print(m1.dot(m2))

# m1 = Matrix([[1, 2, 3], [4, 5, 6]], 2, 3)
# m2 = Matrix([[3, 4, 5], [6, 7, 8]], 2, 3)
# print(m1.in1d([2, 5, 8]))
# print(m1.unique())
# print(m1.intersect1d(m2))
# print(m1.union1d(m2))

# m = Matrix([[1, 2, 3], [4, 5, 6]], 2, 3)
# print(m.sum())
# print(m.sum(axis=0))
# print(m.cumsum())
# print(m.cumsum(axis=1))
# print(m.mean())
# print(m.mean(axis=1))

a = Matrix.arrange(11)
b = a[1:2]
# c = Matrix.arrange(100).reshape((10, 10))
# d = c[::2, ::2]
