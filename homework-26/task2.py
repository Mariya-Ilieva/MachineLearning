import sys
import datetime

DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

class Filter:
    def filter(self, record):
        return True

class StreamHandler:
    def __init__(self, level=DEBUG, filter=None):
        self.level = level
        self.formatter = None
        self.filter = filter

    def setLevel(self, level):
        self.level = level

    def setFormatter(self, formatter):
        self.formatter = formatter

    def setFilter(self, filter):
        self.filter = filter

    def emit(self, record):
        if record.level >= self.level and (self.filter is None or self.filter.filter(record)):
            message = self.formatter.format(record)
            sys.stdout.write(message + '\n')

class FileHandler(StreamHandler):
    def __init__(self, filename, mode='w', level=DEBUG, filter=None):
        super().__init__(level, filter)
        self.filename = filename
        self.mode = mode
        self.file = None

    def open_file(self):
        if self.filename:
            self.file = open(self.filename, self.mode)

    def close_file(self):
        if self.file:
            self.file.close()

    def emit(self, record):
        if record.level >= self.level and (self.filter is None or self.filter.filter(record)):
            message = self.formatter.format(record)
            sys.stdout.write(message + '\n')

            if self.file:
                self.file.write(message + '\n')

class Formatter:
    def __init__(self, fmt):
        self.fmt = fmt

    def format(self, record):
        return self.fmt % {
            'asctime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'name': record.name,
            'levelname': record.levelname,
            'message': record.msg,
        }

class LogRecord:
    def __init__(self, name, level, msg):
        self.name = name
        self.level = level
        self.msg = msg
        self.levelname = self.getLevelName(level)

    def getLevelName(self, level):
        for key, value in globals().items():
            if key.isupper() and value == level:
                return key
        return 'Level %d' % level

class Logger:
    def __init__(self, name):
        self.name = name
        self.handlers = []
        self.level = DEBUG
        self.parent = None
        self.filters = []

    def setLevel(self, level):
        self.level = level

    def addHandler(self, handler):
        self.handlers.append(handler)

    def addFilter(self, filter):
        self.filters.append(filter)

    def propagate(self, record):
        if self.parent:
            self.parent.propagate(record)

    def apply_filters(self, record):
        for filter in self.filters:
            if not filter.filter(record):
                return False

        return True

    def log(self, level, msg):
        record = LogRecord(self.name, level, msg)

        if self.apply_filters(record):
            for handler in self.handlers:
                if self.level <= level <= handler.level:
                    handler.emit(record)

            self.propagate(record)

    def debug(self, msg):
        self.log(DEBUG, msg)

    def info(self, msg):
        self.log(INFO, msg)

    def warning(self, msg):
        self.log(WARNING, msg)

    def error(self, msg):
        self.log(ERROR, msg)

    def critical(self, msg):
        self.log(CRITICAL, msg)


if __name__ == '__main__':
    root_logger = Logger('')
    root_logger.setLevel(DEBUG)

    handler = StreamHandler()
    handler.setLevel(DEBUG)

    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    root_logger.addHandler(handler)

    logger = Logger('my_logger')
    logger.parent = root_logger

    handler = StreamHandler()
    handler.setLevel(DEBUG)

    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.setLevel(INFO)


    class MyFilter(Filter):
        def filter(self, record):
            return record.levelname != 'ERROR'


    my_filter = MyFilter()
    logger.addFilter(my_filter)

    logger.debug('DEBUG message')
    logger.info('INFO message')
    logger.warning('WARNING message')
    logger.error('ERROR message')
    logger.critical('CRITICAL message')
