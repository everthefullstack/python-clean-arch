from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.carteira import Carteira
from sqlmodel import Session


@dataclass(slots=True, kw_only=True)
class CarteiraRepositoryInterface(ABC):

    @abstractmethod
    def insert_carteira(self, carteira: Carteira, session: Session) -> Carteira:
        pass

@dataclass(slots=True, kw_only=True)
class CarteiraCreateUseCaseInterface(ABC):

    @abstractmethod
    def carteira_create(self, carteira: Carteira, session: Session) -> Carteira:
        pass
