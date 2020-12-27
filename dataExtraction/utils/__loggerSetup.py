import logging
import sys


def configureLogger(logFile: str):
    logFormat = '[%(levelname)s] %(asctime)s %(message)s'
    dateFormat = '%Y-%m-%d %H:%M:%S %z'

    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(logFormat, datefmt=dateFormat)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.FileHandler(logFile)
    handler.setLevel(logging.NOTSET)
    formatter = logging.Formatter(logFormat, datefmt=dateFormat)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
