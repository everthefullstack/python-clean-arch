from dataclasses import dataclass
from sqlmodel import Session, select
from app.domain.entities.carteira import Carteira
from app.infra.models.carteira import CarteiraModel
from app.application.interfaces.carteira import CarteiraRepositoryInterface
from app.presentation.adapters.cadastro import entity_to_model, model_to_entity


@dataclass(slots=True, kw_only=True)
class CarteiraRepository(CarteiraRepositoryInterface):

    session: Session

    def insert_carteira(self, carteira: Carteira) -> CarteiraModel:
        with self.session as session:
            carteira_model: CarteiraModel = entity_to_model(carteira)
            session.add(carteira_model)
            session.commit()
            session.refresh(carteira_model)
            return model_to_entity(carteira_model)

    def select_carteira(self, id: int) -> Carteira | None:
        with self.session as session:
            query = select(CarteiraModel).where(CarteiraModel.id == id)
            carteira_model: CarteiraModel | None = session.scalar(statement=query)
            return model_to_entity(carteira_model)