class Range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def contains(self, n):
        return self.start <= n <= self.end

    def overlaps(self, r):
        return self.start <= r.end and r.start <= self.end

    def merge(self, r):
        if self.overlaps(r):
            self.start = min(self.start, r.start)
            self.end = max(self.end, r.end)
            return True
        else:
            return False

    def __str__(self):
        return f'[{self.start}, {self.end}]'


class Matrix:
    def __init__(self, cols, rows, default_value=0):
        self.cols = cols
        self.rows = rows
        self.matrix = [[default_value] * cols for _ in range(rows)]

    def set(self, x, y, value):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.matrix[y][x] = value
        else:
            raise IndexError

    def get(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.matrix[y][x]
        else:
            raise IndexError

    def submatrix(self, columns, rows):
        if isinstance(columns, (list, tuple, slice, range)) and isinstance(rows, (list, tuple, slice, range)):
            columns_start = columns.start if isinstance(columns, slice) else columns[0]
            columns_end = columns.stop if isinstance(columns, slice) else columns[1]
            rows_start = rows.start if isinstance(rows, slice) else rows[0]
            rows_end = rows.stop if isinstance(rows, slice) else rows[1]

            sub_matrix = Matrix(columns_end - columns_start + 1, rows_end - rows_start + 1)

            for i in range(columns_start, columns_end + 1):
                for j in range(rows_start, rows_end + 1):
                    sub_matrix.set(i - columns_start, j - rows_start, self.get(i, j))

            return sub_matrix

        else:
            raise TypeError('Invalid input types for columns and rows')

    def __getitem__(self, key):
        if isinstance(key, tuple):
            if len(key) == 2:
                x, y = key
                return self.get(x, y)
            elif len(key) == 1:
                row_index = key[0]
                return self.matrix[row_index]
        else:
            raise TypeError('Invalid index type')

    def __setitem__(self, key, value):
        if isinstance(key, tuple) and len(key) == 2:
            x, y = key
            self.set(x, y, value)
        else:
            raise TypeError('Invalid index type')

    def __mul__(self, scalar):
        result_matrix = Matrix(self.cols, self.rows)

        for i in range(self.rows):
            for j in range(self.cols):
                result_matrix.set(j, i, self.get(j, i) * scalar)

        return result_matrix

    def __rmul__(self, scalar):
        return self * scalar

    def __str__(self):
        result = ''

        for row in self.matrix:
            result += ' '.join(map(str, row)) + '\n'

        return result.strip()
