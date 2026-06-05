import logging
import os

from core.config import config


def logger_setup():
    os.makedirs(config.LOG_FOLDER, exist_ok=True)

    logger = logging.getLogger(__name__)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(config.LOG_FILE, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)

    logger.addHandler(console_handler)

    return logger


log = logger_setup()
