from dataclasses import dataclass
from abc import ABC, abstractmethod
from dynaconf import Dynaconf


@dataclass(slots=True, kw_only=True)
class SettingsInterface(ABC):

    @abstractmethod
    def get_settings(self) -> Dynaconf:
        pass
    