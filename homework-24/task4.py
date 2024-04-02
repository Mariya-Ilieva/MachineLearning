class Matrix:
    def __init__(self, rows, cols, fill):
        self.rows = rows
        self.cols = cols
        self.data = ([fill(x, y) for y in range(cols)] for x in range(rows))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


m1 = Matrix(4, 4, lambda x, y: 1)
print(m1)
print('\n')

m2 = Matrix(4, 4, lambda x, y: 1 if x == y else 0)
print(m2)
print('\n')

m3 = Matrix(4, 4, lambda x, y: x + 1 if x == y else 0)
print(m3)
print('\n')

m4 = Matrix(4, 4, lambda x, y: -1 if x > y else 1 if x < y else 0)
print(m4)
print('\n')

m5 = Matrix(4, 4, lambda x, y: abs(x - y))
print(m5)
print('\n')

m6 = Matrix(4, 4, lambda x, y: format(x * 4 + y, 'x'))
print(m6)
print('\n')
