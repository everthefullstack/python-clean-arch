from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.cadastro import Cadastro
from sqlmodel import Session


@dataclass(slots=True, kw_only=True)
class CadastroRepositoryInterface(ABC):

    @abstractmethod
    def insert_cadastro(self, cadastro: Cadastro, session: Session) -> Cadastro:
        pass
    
    @abstractmethod
    def select_cadastro(self, id: int, session: Session) -> Cadastro | None:
        pass

@dataclass(slots=True, kw_only=True)
class CadastroCreateUseCaseInterface(ABC):

    @abstractmethod
    def cadastro_create(self, cadastro: Cadastro, session: Session) -> Cadastro:
        pass

@dataclass(slots=True, kw_only=True)
class CadastroGetUseCaseInterface(ABC):

    @abstractmethod
    def cadastro_get(self, id: int, session: Session) -> Cadastro | None:
        pass