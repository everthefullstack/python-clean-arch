from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.carteira import Carteira


@dataclass(slots=True, kw_only=True)
class CarteiraRepositoryInterface(ABC):

    @abstractmethod
    def insert_carteira(self, carteira: Carteira) -> Carteira:
        pass

    @abstractmethod
    def select_carteira(self, id: int) -> Carteira | None:
        pass

@dataclass(slots=True, kw_only=True)
class CarteiraUseCaseInterface(ABC):

    @abstractmethod
    def insert_carteira(self, carteira: Carteira) -> Carteira:
        pass

    @abstractmethod
    def select_carteira(self, id: int) -> Carteira | None:
        pass