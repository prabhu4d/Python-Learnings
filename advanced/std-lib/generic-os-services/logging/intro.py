import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


# Varibales
name = "Ammu"

logging.error(f"{name} Name Error")


# exception logging
a = 10
b = 0

try:
    a/b
except Exception as e:
    logging.error("Exception Occured", exc_info=True)