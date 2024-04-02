import logging
import logging.config

def logging_fileConfig(file_name):
    config = {}

    try:
        # logging.config.fileConfig(file_name, disable_existing_loggers=False)
        with open(file_name, 'r') as f:
            for line in f:
                parts = line.strip().split('=')

                if len(parts) == 2:
                    k, v = map(str.strip, parts)
                    config[k] = v

        config['version'] = 1

        logging.config.dictConfig(config)

        print('Logging')


    except FileNotFoundError:
        print(f'Error configuring logging: File "{file_name}" not found.')

    except PermissionError:
        print(f'"Error configuring logging: Permission denied for file "{file_name}"."')

    except Exception as e:
        print(f'Error configuring logging: {e}')

logging_fileConfig('log-config.ini')

logger = logging.getLogger(__name__)

logger.warning('This is a warning')
logger.error('This is an error')
