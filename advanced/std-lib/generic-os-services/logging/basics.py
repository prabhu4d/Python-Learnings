import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(filename)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("basic.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        # logger.error("Tried to divide by zero")
        logger.exception("Tried to divide by zero")


result = [add(10, 20), sub(10, 20), mul(10, 20), div(10, 0)]

logger.debug(f"Add : 10, 20 = {result[0]}")
logger.debug(f"Sub : 10, 20 = {result[1]}")
logger.debug(f"Mul : 10, 20 = {result[2]}")
logger.debug(f"Div : 10, 20 = {result[3]}")
