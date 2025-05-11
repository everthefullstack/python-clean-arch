from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.transferencia import Transferencia


@dataclass(slots=True)
class TransferenciaRepositoryInterface(ABC):

    @abstractmethod
    def insert_transferencia(self, transferencia: Transferencia) -> Transferencia:
        pass

@dataclass(slots=True)
class TransferenciaCreateUseCaseInterface(ABC):

    @abstractmethod
    def transferencia_create(self, transferencia: Transferencia) -> Transferencia | None:
        pass
    