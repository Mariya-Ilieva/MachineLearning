import sys
import datetime
from abc import ABC, abstractmethod

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

class Handler(ABC):
    def __init__(self, level=DEBUG, formatter=None):
        self.level = level
        self.formatter = formatter

    def setLevel(self, level):
        self.level = level

    def setFormatter(self, formatter):
        self.formatter = formatter

    @abstractmethod
    def emit(self, record):
        pass

class StreamHandler(Handler):
    def __init__(self, parent_logger=None, level=DEBUG, formatter=None):
        super().__init__(level, formatter)
        self.parent_logger = parent_logger
        self.level = level
        self.formatter = None

    def emit(self, record):
        if self.formatter:
            message = self.formatter.format(record)
        else:
            message = record.msg

        if record.level >= self.level:
            sys.stdout.write(message + '\n')

        if self.parent_logger:
            self.parent_logger.propagate(record)


class FileHandler(Handler):
    def __init__(self, filename, mode='w', level=DEBUG, formatter=None):
        super().__init__(level, formatter)
        self.filename = filename
        self.mode = mode

    def emit(self, record):
        with open (self.filename, self.mode) as file:
            file.write(record.msg + '\n')


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


class Filter(ABC):
    def __init__(self, name):
        self.name = name

    def filter(self, record):
        if 'ERROR' in record.msg:
            return False

        return True


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
    def __init__(self, name, parent_loger=None, filters=None):
        self.name = name
        self.parent_loger = parent_loger
        self.handlers = []
        self.level = DEBUG
        self.filters = filters or []

    def setLevel(self, level):
        self.level = level

    def setParentLogger(self, parent_logger):
        self.parent_loger = parent_logger

        if parent_logger:
            self.level = parent_logger.level

    def addHandler(self, handler):
        self.handlers.append(handler)

        if self.parent_loger:
            self.parent_loger.addHandler(handler)

    def propagate(self, record):
        if self.parent_loger:
            self.parent_loger.log(record.level, record.msg)

            if self.parent_loger:
                self.parent_loger.propagate(record)


    def log(self, level, msg):
        record = LogRecord(self.name, level, msg)

        if all(filter.filter(record) for filter in self.filters):
            for handler in self.handlers:
                if (self.level <= level and getattr(handler, 'filters', None)
                                        and all(filter.filter(record) for filter in handler.filters)):
                    handler.emit(record)

            if self.parent_loger and self.propagate:
                self.parent_loger.log(level, msg)

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
    root_logger = Logger('root')
    root_logger.setLevel(level)

    stream_handler = StreamHandler()
    stream_handler.setLevel(level)

    formatter = Formatter(format_str)
    stream_handler.setFormatter(formatter)

    root_logger.addHandler(stream_handler)

    filter_instance = Filter('my_filter')
    stream_handler = StreamHandler()
    stream_handler.filters = [filter_instance]

    return root_logger


def dictConfig(config):
    loggers_config = config.get('loggers', {})

    for logger_name, logger_config in loggers_config.items():
        logger = Logger(logger_name)

        level_str = logger_config.get('level', '')
        logger.setLevel(level_str or WARNING)

        handlers_config = config.get('handlers', {})
        for handler_name in logger_config.get('handlers', []):
            handler_config = handlers_config.get(handler_name, {})

            handler_class = globals()[handler_config.get('class', '')]
            handler_level = handler_config.get('level', '') or WARNING
            handler_formatter = config['formatters'].get(handler_config.get('formatter', ''))

            handler_instance = handler_class(level=handler_level, formatter=handler_formatter)

            logger.addHandler(handler_instance)

if __name__ == '__main__':
    config = {
        'version': 1,
        'handlers': {
            'stream_handler': {
                'class': 'StreamHandler',
                'level': 'DEBUG',
                'formatter': 'custom_formatter',
            },
        },
        'formatters': {
            'custom_formatter': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'loggers': {
            'root': {
                'level': 'DEBUG',
                'handlers': ['stream_handler'],
            },
        },
    }

    dictConfig(config)

    root_logger = Logger('root')
    root_logger.setLevel(DEBUG)

    stream_handler = StreamHandler()
    stream_handler.setLevel(DEBUG)

    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)

    root_logger.addHandler(stream_handler)

    file_handler = FileHandler('logfile.txt', mode='a', level=DEBUG, formatter=formatter)
    root_logger.addHandler(file_handler)

    child_logger = Logger('child')
    child_logger.setLevel(DEBUG)

    grandchild_logger = Logger('grandchild')
    grandchild_logger.setLevel(DEBUG)

    debug('DEBUG message from global function')
    child_logger.info('INFO message from child logger')
    grandchild_logger.warning('WARNING message from grandchild logger')
