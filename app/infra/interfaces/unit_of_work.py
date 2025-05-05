from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class UnitOfWorInterface(ABC):

    @abstractmethod
    def __enter__(self) -> "UnitOfWorInterface":
        pass
    
    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass
