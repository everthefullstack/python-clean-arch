from app.domain.entities.carteira import Carteira
from app.infra.models.carteira import CarteiraModel


def entity_to_model(carteira: Carteira) -> CarteiraModel:
    return CarteiraModel(
        id=carteira.id,
        saldo=carteira.saldo,
        carteira_id=carteira.carteira_id,
    )

def model_to_entity(carteira_model: CarteiraModel) -> Carteira:
    return Carteira(
        id=carteira_model.id,
        saldo=carteira_model.saldo,
        carteira_id=carteira_model.carteira_id,
    )