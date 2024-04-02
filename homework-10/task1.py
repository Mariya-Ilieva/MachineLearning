class Matrix:
    def __init__(self, cols, rows, default_value=None):
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


m = Matrix(2, 2, 0)
m.set(0, 1, 15)
v1 = m.get(0, 1)
v2 = m.get(0, 0)

print(v1)
print(v2)
