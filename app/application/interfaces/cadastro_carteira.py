from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.cadastro import Cadastro


@dataclass(slots=True)
class CadastroCarteiraCreateUseCaseInterface(ABC):

    @abstractmethod
    def cadastro_carteira_create(self, id: int) -> Cadastro | None:
        pass
    