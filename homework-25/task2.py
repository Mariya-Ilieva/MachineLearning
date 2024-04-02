from logging import *


logger = Logger(__name__)

c_handler = StreamHandler()
f_handler = FileHandler('file.log')
c_handler.setLevel(WARNING)
f_handler.setLevel(ERROR)

c_format = Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
