from dataclasses import dataclass
from sqlmodel import Session
from app.domain.entities.carteira import Carteira
from app.infra.models.carteira import CarteiraModel
from app.application.interfaces.carteira import CarteiraRepositoryInterface
from app.presentation.adapters.carteira import entity_to_model, model_to_entity


@dataclass(slots=True, kw_only=True)
class CarteiraRepository(CarteiraRepositoryInterface):

    session: Session | None = None

    def insert_carteira(self, carteira: Carteira) -> CarteiraModel:
        carteira_model: CarteiraModel = entity_to_model(carteira)
        self.session.add(carteira_model)
        self.session.flush()
        return model_to_entity(carteira_model)
