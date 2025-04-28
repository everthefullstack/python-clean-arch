from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.cadastro import Cadastro


@dataclass(slots=True, kw_only=True)
class CadastroRepositoryInterface(ABC):

    @abstractmethod
    def insert_cadastro(self, cadastro: Cadastro) -> Cadastro:
        pass
    
    @abstractmethod
    def select_cadastro(self, id: int) -> Cadastro | None:
        pass

@dataclass(slots=True, kw_only=True)
class CadastroUseCaseInterface(ABC):

    @abstractmethod
    def create_cadastro(self, cadastro: Cadastro) -> Cadastro:
        pass
    
    @abstractmethod
    def get_cadastro(self, id: int) -> Cadastro | None:
        pass