from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional


#classe abstrata
@dataclass(slots=True, kw_only=True)
class CadastroAbc(ABC):

    id: Optional[int] = field(default=None)
    nome: str
    documento: str
    email: str
    senha: str

    @abstractmethod
    def valida_documento(self) -> None:
        pass

    @abstractmethod
    def faz_transferencia(self) -> bool:
        pass
