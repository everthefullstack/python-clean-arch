from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(slots=True, kw_only=True)
class TransferenciaValExtInterface(ABC):

    @abstractmethod
    def validar_transferencia(self) -> bool:
        pass
    