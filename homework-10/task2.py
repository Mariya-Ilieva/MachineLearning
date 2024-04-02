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

    def subMatrix(self, columns, rows):
        if not isinstance(columns, Range) or not isinstance(rows, Range):
            raise TypeError

        sub_matrix = Matrix(columns.end - columns.start + 1, rows.end - rows.start + 1)

        for i in range(columns.start, columns.end + 1):
            for j in range(rows.start, rows.end + 1):
                sub_matrix.set(i - columns.start, j - rows.start, self.get(i, j))

        return sub_matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += ' '.join(map(str, row)) + '\n'
        return result.strip()


m = Matrix(4, 4)
for i in range(4):
    m.set(i, i, i + 1)

cols = Range(1, 2)
rows = Range(2, 3)
m2 = m.subMatrix(cols, rows)

print(m2)
