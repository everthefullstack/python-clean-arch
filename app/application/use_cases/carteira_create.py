from dataclasses import dataclass
from app.domain.entities.carteira import Carteira
from app.application.interfaces.carteira import CarteiraCreateUseCaseInterface, CarteiraRepositoryInterface
from sqlmodel import Session


@dataclass(slots=True, kw_only=True)
class CarteiraCreateUseCase(CarteiraCreateUseCaseInterface):

    carteira_repository: CarteiraRepositoryInterface
    
    def carteira_create(self, carteira: Carteira, session: Session):
        carteira = self.carteira_repository.insert_carteira(carteira=carteira, session=session)
        return carteira
