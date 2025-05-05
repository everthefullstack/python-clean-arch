import logging
from dataclasses import dataclass
from app.infra.settings.settings import settings
from app.infra.utils.singleton import singleton


@singleton
@dataclass
class LogManager:

    __name: str = settings.get_settings().APP_NAME

    def create_logger(self) -> logging.Logger:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        logger = logging.getLogger(self.__name)
        logger.setLevel(logging.INFO)

        return logger

logger: LogManager = LogManager()
    