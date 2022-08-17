import daemon
import time
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


def task():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler('my_logger.log', maxBytes=2000, backupCount=10)
    logger.addHandler(handler)

    while True:
        logger.info('This is an info message' + str(datetime.now()))
        time.sleep(5)


def daemonize():
    with daemon.DaemonContext():
        task()


if __name__ == "__main__":
    task()
