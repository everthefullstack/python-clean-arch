from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any


@dataclass(slots=True, kw_only=True)
class SessionInterface(ABC):

    @abstractmethod
    def get_session(self) -> Any:
        pass
    