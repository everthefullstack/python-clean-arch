import logging
from dataclasses import dataclass


@dataclass
class LoggerManager:

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        return logging.getLogger(name)