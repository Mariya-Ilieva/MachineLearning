from array import array

class Matrix:
    def __init__(self, cols, rows, default_value=0, dtype='L'):
        self.cols = cols
        self.rows = rows

        valid_types = {
            'int8': 'b',
            'int16': 'h',
            'int32': 'i',
            'int64': 'q',
            'uint8': 'B',
            'uint16': 'H',
            'uint32': 'I',
            'uint64': 'Q',
            'float16': 'e',
            'float32': 'f',
            'float64': 'd',
            'bool': '?',
            'byte': 'b',
            'short': 'h',
            'intc': 'i',
            'int_': 'l',
            'long': 'l',
            'longlong': 'q',
            'ubyte': 'B',
            'ushort': 'H',
            'uintc': 'I',
            'uint': 'L',
            'ulong': 'L',
            'ulonglong': 'Q',
            'half': 'e',
            'single': 'f',
            'double': 'd',
            'longdouble': 'g',
            'csingle': 'F',
            'cdouble': 'D',
            'clongdouble': 'G',
        }

        if dtype not in valid_types:
            raise ValueError(f'Invalid dtype "{dtype}".')

        self.matrix = [array(valid_types[dtype], [default_value] * cols) for _ in range(rows)]

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

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += ' '.join(map(str, row)) + '\n'
        return result.strip()


m = Matrix(11, 5, 8, dtype='ushort')
print(m)
