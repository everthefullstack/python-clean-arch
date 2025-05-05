from dataclasses import dataclass
from abc import ABC, abstractmethod
from sqlmodel import Session


@dataclass(slots=True, kw_only=True)
class SessionInterface(ABC):

    @abstractmethod
    def get_session(self) -> Session:
        pass
    