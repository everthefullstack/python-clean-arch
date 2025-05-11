from dataclasses import dataclass
from sqlmodel import Session, update
from app.domain.entities.carteira import Carteira
from app.infra.models.carteira import CarteiraModel
from app.application.interfaces.carteira import CarteiraRepositoryInterface
from app.presentation.adapters.carteira import entity_to_model, model_to_entity
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class CarteiraRepository(CarteiraRepositoryInterface):

    session: Session | None = None

    def insert_carteira(self, carteira: Carteira) -> CarteiraModel:
        lg.info("Executando a função insert_carteira do CarteiraRepository")

        carteira_model: CarteiraModel = entity_to_model(carteira)
        self.session.add(carteira_model)
        self.session.flush()
        return model_to_entity(carteira_model)
    
    def update_saldo(self, carteira: Carteira) -> CarteiraModel:
        lg.info("Executando a função update_saldo do CarteiraRepository")
        
        stmt = (update(CarteiraModel)
                .where(CarteiraModel.id == carteira.id)
                .values(saldo=carteira.saldo
            )
        )
        self.session.exec(stmt)
        self.session.flush()
        