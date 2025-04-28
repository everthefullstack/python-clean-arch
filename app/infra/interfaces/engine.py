from dataclasses import dataclass
from abc import ABC, abstractmethod
from sqlalchemy.engine import Engine


@dataclass(slots=True, kw_only=True)
class EngineInterface(ABC):

    @abstractmethod
    def get_engine(self) -> Engine:
        pass
    