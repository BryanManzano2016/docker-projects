import daemon
import time
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os


def task():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler('logger.log', maxBytes=10000, backupCount=2)
    logger.addHandler(handler)

    while True:
        logger.info(os.environ['ID_APP'] + ' - This is an info message - ' + str(datetime.now()))
        time.sleep(5)


def daemonize():
    with daemon.DaemonContext():
        task()


if __name__ == "__main__":
    task()
