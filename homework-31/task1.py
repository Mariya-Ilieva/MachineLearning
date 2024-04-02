import io
import sys


DEFAULT_BUFFER_SIZE = 4096


class BufferedReader:
    def __init__(self, raw_file, buffer_size=DEFAULT_BUFFER_SIZE):
        self.raw_file = raw_file
        self.buffer = b''
        self.buffer_size = buffer_size

    def close(self):
        self.raw_file.close()

    def read(self, size=-1):
        if size == -1:
            size = self.buffer_size

        while len(self.buffer) < size:
            part = self.raw_file.read(self.buffer_size)

            if not part:
                break

            self.buffer += part

        result = self.buffer[:size]
        self.buffer = self.buffer[size:]

        return result

    def reset_buffer(self):
        self.buffer = b''


class TextIOWrapper:
    def __init__(self, buffer, encoding='utf-8'):
        self.buffer = buffer
        self.encoding = encoding

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.buffer.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.readline()

        if not line:
            raise StopIteration

        return line

    def readline(self, size=-1):
        if size == -1:
            size = sys.maxsize

        line = b''

        while True:
            char = self.buffer.read(1)

            if not char or char == b'\n' or len(line) == size + 1:
                break

            line += char

        return line.decode(self.encoding)


raw = io.FileIO('filename.txt', 'r')
reader = BufferedReader(raw)
file = TextIOWrapper(reader, encoding='utf-8')

with file:
    for line in file:
        print(line)
