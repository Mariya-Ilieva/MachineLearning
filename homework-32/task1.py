DEFAULT_BUFFER_SIZE = 4096


class BufferedReader:
    def __init__(self, raw_file, buffer_size=DEFAULT_BUFFER_SIZE):
        self.raw_file = raw_file
        self.buffer = bytearray()
        self.buffer_size = buffer_size

    def close(self):
        self.raw_file.close()

    def readinto(self, b):
        view = memoryview(b)
        size = len(view)

        while len(self.buffer) < size:
            part = self.raw_file.read(self.buffer_size)

            if not part:
                break

            self.buffer.extend(part)

        view[:len(self.buffer)] = self.buffer
        self.buffer = self.buffer[size:]

        return len(view)

    def reset_buffer(self):
        self.buffer = bytearray()
