from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(slots=True, kw_only=True)
class DatabaseInterface(ABC):

    @abstractmethod
    def create_database(self) -> None:
        pass
