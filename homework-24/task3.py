class Matrix:
    def __init__(self, rows, cols, matrix_data):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix_data

    def __str__(self):
        max_widths = [0] * self.cols

        for row in self.matrix:
            for j in range(self.cols):
                max_widths[j] = max(max_widths[j], len(str(row[j])))

        output = ''
        for i in range(self.rows):
            for j in range(self.cols):
                el = str(self.matrix[i][j])
                el = el.rjust(max_widths[j])

                output += el

                if j < self.cols - 1:
                    output += ' '

            if i < self.rows - 1:
                output += '\n'

        return output


m = Matrix(3, 3, [[1, 11, 123], [21, 4, 7], [3, 34, 2222]])
print(m)
print('\n')

m = Matrix(3, 3, [[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
print(m)
