import time
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os
import requests


def task():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler('logger.log', maxBytes=10000, backupCount=2)
    logger.addHandler(handler)

    while True:
        res = requests.get(os.environ['URL_SERVER'])
        logger.info(os.environ['URL_SERVER'] + " - " + os.environ['ID_APP'] + ' - This is an info message - ' +
                    str(datetime.now()) + " - " + str(res.text)[0:25])
        time.sleep(5)


if __name__ == "__main__":
    task()
