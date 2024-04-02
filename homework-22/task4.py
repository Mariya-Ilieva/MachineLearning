from array import array


class Matrix:
    def __init__(self, *, data=None, cols=None, rows=None, fill=None, default_value=0, dtype='b'):
        if data is not None:
            self.rows = len(data)
            self.cols = len(data[0]) if self.rows > 0 else 0
            self.dtype = dtype
            self.matrix = array(self.dtype, [el for row in data for el in row])

        elif cols is not None and rows is not None:
            self.rows = rows
            self.cols = cols
            self.dtype = dtype

            list = [fill(x, y) for y in range(rows) for x in range(cols)] if fill else \
                [default_value] * (rows * cols)

            self.matrix = array(self.dtype, list)

        else:
            raise ValueError("Please provide either 'data' or 'cols' and 'rows'.")

    @property
    def shape(self):
        return self.rows, self.cols

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
        output = '['

        for i in range(self.rows):
            output += '[' + ', '.join(map(str, self.matrix[i * self.cols:(i + 1) * self.cols])) + '],\n'
        output = output.rstrip(',\n')

        output += ']'

        return output


m = Matrix(data=[[1, 2, 3], [4, 5, 6]])
print(m)
print(m.shape)
