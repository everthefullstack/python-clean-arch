from dataclasses import dataclass
from app.infra.interfaces.logger import LoggerInterface
from app.infra.utils.singleton import singleton
import logging as lg


@singleton
@dataclass(slots=True, kw_only=True)
class LoggerManager(LoggerInterface):
    __logger: lg.Logger | None = None
        
    def __post_init__(self) -> None:
        lg.basicConfig(
            level=lg.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.__logger = lg.getLogger("LoggerManager")

    def info(self, message: str) -> None:
        self.__logger.info(message)

    def error(self, message: str) -> None:
        self.__logger.error(message)

    def warning(self, message: str) -> None:
        self.__logger.warning(message)

    def debug(self, message: str) -> None:
        self.__logger.debug(message)

logger: LoggerManager = LoggerManager()