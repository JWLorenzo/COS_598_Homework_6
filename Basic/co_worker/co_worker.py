import logging
import os
from redis import Redis
import requests
import time
import random

DEBUG = os.environ.get("DEBUG", "").lower().startswith("y")
log = logging.getLogger(__name__)
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)


def bother() -> None:
    sleep: float = random.random() + 0.5
    time.sleep(sleep)
    log.info("Being a bother")

    response = requests.get("http://worker/")


if __name__ == "__main__":
    while True:
        try:
            bother()
        except Exception as e:
            log.info(f"Hit the error{e}")
