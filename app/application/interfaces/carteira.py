from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entities.carteira import Carteira


@dataclass(slots=True)
class CarteiraRepositoryInterface(ABC):

    @abstractmethod
    def insert_carteira(self, carteira: Carteira) -> Carteira:
        pass
