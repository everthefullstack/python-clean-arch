from app.domain.entities.cadastro import Cadastro
from app.infra.models.cadastro import CadastroModel


def entity_to_model(cadastro: Cadastro) -> CadastroModel:
    return CadastroModel(
        nome=cadastro.nome,
        documento=cadastro.documento,
        email=cadastro.email,
        senha=cadastro.senha,
        tipo_cadastro=cadastro.tipo_cadastro,
    )

def model_to_entity(cadastro_model: CadastroModel) -> Cadastro:
    return Cadastro(
        id=cadastro_model.id,
        nome=cadastro_model.nome,
        documento=cadastro_model.documento,
        email=cadastro_model.email,
        senha=None,
        tipo_cadastro=cadastro_model.tipo_cadastro,
        carteira=cadastro_model.carteira,
    )