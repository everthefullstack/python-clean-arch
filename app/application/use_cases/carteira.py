from dataclasses import dataclass
from app.domain.entities.carteira import Carteira
from app.application.interfaces.carteira import CarteiraUseCaseInterface, CarteiraRepositoryInterface


@dataclass(slots=True, kw_only=True)
class CarteiraUseCase(CarteiraUseCaseInterface):

    carteira_repository: CarteiraRepositoryInterface
    
    def create_carteira(self, carteira: Carteira):
        self.carteira_repository.insert_carteira(carteira=carteira)
        
    def get_carteira(self, id: int) -> Carteira:
        self.carteira_repository.select_carteira(id=id)
