from dataclasses import dataclass
from sqlmodel import Session
from app.domain.entities.carteira import Carteira
from app.infra.models.carteira import CarteiraModel
from app.application.interfaces.carteira import CarteiraRepositoryInterface
from app.presentation.adapters.carteira import entity_to_model, model_to_entity


@dataclass(slots=True, kw_only=True)
class CarteiraRepository(CarteiraRepositoryInterface):

    def insert_carteira(self, carteira: Carteira, session: Session) -> CarteiraModel:
        carteira_model: CarteiraModel = entity_to_model(carteira)
        session.add(carteira_model)
        session.flush()
        session.refresh(carteira_model)
        return model_to_entity(carteira_model)
