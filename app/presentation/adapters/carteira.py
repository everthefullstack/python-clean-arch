from app.domain.entities.carteira import Carteira
from app.infra.models.carteira import CarteiraModel
from app.infra.logger.logger import logger as lg


def entity_to_model(carteira: Carteira) -> CarteiraModel:
    lg.info("Executando a função entity_to_model do adaptador Carteira")

    return CarteiraModel(
        id=carteira.id,
        saldo=carteira.saldo,
        cadastro_id=carteira.cadastro_id,
    )

def model_to_entity(carteira_model: CarteiraModel) -> Carteira:
    lg.info("Executando a função model_to_entity do adaptador Carteira")
    
    return Carteira(
        id=carteira_model.id,
        saldo=carteira_model.saldo,
        cadastro_id=carteira_model.cadastro_id,
    )