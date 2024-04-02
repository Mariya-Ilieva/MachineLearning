import sys
import datetime

DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

def debug(msg):
    root_logger.debug(msg)

def info(msg):
    root_logger.info(msg)

def warning(msg):
    root_logger.warning(msg)

def error(msg):
    root_logger.error(msg)

def critical(msg):
    root_logger.critical(msg)


class StreamHandler:
    def __init__(self, parent_logger=None, level=DEBUG, handler_level=DEBUG):
        self.level = level
        self.formatter = None
        self.parent_logger = parent_logger
        self.handler_level = handler_level

    def setLevel(self, level):
        self.level = level

    def setFormatter(self, formatter):
        self.formatter = formatter

    def emit(self, record):
        if self.formatter:
            message = self.formatter.format(record)
        else:
            message = record.msg

        if record.level >= self.level:
            sys.stdout.write(message + '\n')

        if self.parent_logger:
            self.parent_logger.propagate(record)


class FileHandler(StreamHandler):
    def __init__(self, filename, mode='w', level=DEBUG, handler_level=DEBUG):
        super().__init__(level=level, handler_level=handler_level)
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
        super().emit(record)

        if self.file:
            self.file.write(record.msg + '\n')


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

        return str(level)


class Logger:
    def __init__(self, name, parent_loger=None):
        self.name = name
        self.parent_loger = parent_loger
        self.handlers = []
        self.level = DEBUG
        self.filter_level = None

    def setFilterLevel(self, level):
        self.filter_level = level

    def addHandler(self, handler, handler_level=None):
        if handler_level is None:
            handler_level = self.level

        handler.handler_level = handler_level
        self.handlers.append(handler)

        if self.parent_loger:
            self.parent_loger.addHandler(handler, handler_level)

    def propagate(self, record):
        if self.parent_loger:
            self.parent_loger.propagate(record)

    def log(self, level, msg):
        record = LogRecord(self.name, level, msg)

        for handler in self.handlers:
            if (self.level <= level <= handler.handler_level and
               (self.filter_level is None or level >= self.filter_level)):
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


def basicConfig(level=DEBUG, format_str='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    root_logger = Logger('')
    root_logger.setFilterLevel(level)

    stream_handler = StreamHandler()
    stream_handler.setLevel(level)

    formatter = Formatter(format_str)
    stream_handler.setFormatter(formatter)

    root_logger.addHandler(stream_handler, handler_level=level)

if __name__ == '__main__':
    root_logger = Logger('')
    root_logger.setFilterLevel(DEBUG)
    root_logger.setFilterLevel(WARNING)

    handler = StreamHandler()
    handler.setLevel(DEBUG)

    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    root_logger.addHandler(handler, handler_level=INFO)

    logger = Logger('my_logger', root_logger)
    logger.addHandler(handler, handler_level=DEBUG)

    logger.debug('DEBUG message')
    logger.info('INFO message')
    logger.warning('WARNING message')
    logger.error('ERROR message')
    logger.critical('CRITICAL message')
