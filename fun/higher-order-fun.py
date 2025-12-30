import logging


def add(x, y, f):
    logging.log(logging.INFO, "add(%s, %s, %s)", x, y, f)

    return f(x) + f(y)
