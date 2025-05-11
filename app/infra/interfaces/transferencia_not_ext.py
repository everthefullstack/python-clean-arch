from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(slots=True, kw_only=True)
class TransferenciaNotExtInterface(ABC):

    @abstractmethod
    def notificar_transferencia(self) -> bool:
        pass
    