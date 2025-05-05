from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.cadastro import Cadastro


@dataclass(slots=True)
class CadastroRepositoryInterface(ABC):

    @abstractmethod
    def insert_cadastro(self, cadastro: Cadastro) -> Cadastro:
        pass
    
    @abstractmethod
    def select_cadastro(self, id: int) -> Cadastro | None:
        pass

@dataclass(slots=True)
class CadastroGetUseCaseInterface(ABC):

    @abstractmethod
    def cadastro_get(self, id: int) -> Cadastro | None:
        pass