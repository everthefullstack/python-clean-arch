from app.domain.entities.transferencia import Transferencia
from app.infra.models.transferencia import TransferenciaModel
from app.infra.logger.logger import logger as lg


def entity_to_model(transferencia: Transferencia) -> TransferenciaModel:
    lg.info("Executando a função entity_to_model do adaptador Transferencia")

    return TransferenciaModel(
        valor=transferencia.valor,
        pagador_id=transferencia.pagador_id,
        recebedor_id=transferencia.recebedor_id,
        data=transferencia.data,
    )

def model_to_entity(transferencia_model: TransferenciaModel) -> Transferencia:
    lg.info("Executando a função model_to_entity do adaptador Transferencia")
    
    return Transferencia(
        id=transferencia_model.id,
        valor=transferencia_model.valor,
        pagador_id=transferencia_model.pagador_id,
        recebedor_id=transferencia_model.recebedor_id,
        data=transferencia_model.data,
    )
