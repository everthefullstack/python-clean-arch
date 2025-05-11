from dataclasses import dataclass
from sqlmodel import Session, select
from app.domain.entities.transferencia import Transferencia
from app.infra.models.transferencia import TransferenciaModel
from app.application.interfaces.transferencia import TransferenciaRepositoryInterface
from app.presentation.adapters.transferencia import entity_to_model, model_to_entity
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class TransferenciaRepository(TransferenciaRepositoryInterface):

    session: Session | None = None

    def insert_transferencia(self, transferencia: Transferencia) -> Transferencia:
        lg.info("Executando a função insert_transferencia do TransferenciaRepository")
        
        transferencia_model: TransferenciaModel = entity_to_model(transferencia)
        self.session.add(transferencia_model)
        self.session.flush()
        return model_to_entity(transferencia_model)
