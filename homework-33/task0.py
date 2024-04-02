import io
import sys


DEFAULT_BUFFER_SIZE = 4096


class BufferedReader:
    def __init__(self, raw_file, buffer_size=DEFAULT_BUFFER_SIZE):
        self.raw_file = raw_file
        self.buffer = bytearray(buffer_size)
        self.buffer_size = buffer_size
        self.buffer_pos = 0

    def close(self):
        self.raw_file.close()

    def readinto(self, b, pos=None):
        view = memoryview(b)
        size = len(view)

        if pos is not None:
            read_size = self.raw_file.readinto(self.buffer, pos)
            self.buffer_pos = 0

            if read_size == 0:
                return

        while self.buffer_pos + size > len(self.buffer):
            read_size = self.raw_file.readinto(self.buffer)
            self.buffer_pos = 0

            if read_size == 0:
                return

        view[:size] = self.buffer[self.buffer_pos:self.buffer_pos + size]
        self.buffer_pos += size

        return size

    def reset_buffer(self):
        self.buffer_pos = 0


class TextIOWrapper:
    def __init__(self, buffer, encoding='utf-8', max_lines=None):
        self.buffer = buffer
        self.encoding = encoding
        self.max_lines = max_lines
        self.line_count = 0

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.buffer.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.readline()

        if not line or (self.max_lines is not None and self.line_count >= self.max_lines):
            raise StopIteration

        self.line_count += 1

        return line

    def readline(self, size=-1):
        if size == -1:
            size = sys.maxsize

        line = b''

        while True:
            char = bytearray(1)
            read_size = self.buffer.readinto(char)

            if not read_size or char == b'\n':
                break

            line += char

        return line.decode(self.encoding)


# raw = io.FileIO('filename.txt', 'r')
# reader = BufferedReader(raw)
# file = TextIOWrapper(reader, encoding='utf-8', max_lines=5)
#
# with file:
#     for line in file:
#         print(line)


DEFAULT_BUFFER_SIZE = 20
buffer = bytearray(DEFAULT_BUFFER_SIZE)

pos = 10
mv = memoryview(buffer)
chunk = mv[pos:]
print(type(chunk))
chunk[0] = 65

print(buffer)
