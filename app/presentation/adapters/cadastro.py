from app.domain.entities.cadastro import Cadastro
from app.domain.entities.carteira import Carteira
from app.infra.models.cadastro import CadastroModel
from app.infra.logger.logger import logger as lg


def entity_to_model(cadastro: Cadastro) -> CadastroModel:
    lg.info("Executando a função entity_to_model do adaptador Cadastro")
    
    return CadastroModel(
        nome=cadastro.nome,
        documento=cadastro.documento,
        email=cadastro.email,
        senha=cadastro.senha,
        tipo_cadastro=cadastro.tipo_cadastro,
    )

def model_to_entity(cadastro_model: CadastroModel) -> Cadastro:
    lg.info("Executando a função model_to_entity do adaptador Cadastro")
    
    carteira = None

    if cadastro_model.carteira:
        carteira = Carteira(
            id=cadastro_model.carteira.id,
            saldo=cadastro_model.carteira.saldo,
            cadastro_id=cadastro_model.carteira.cadastro_id,
        )
    
    else:
        carteira = cadastro_model.carteira

    cadastro = Cadastro(
        id=cadastro_model.id,
        nome=cadastro_model.nome,
        documento=cadastro_model.documento,
        email=cadastro_model.email,
        senha=cadastro_model.senha,
        tipo_cadastro=cadastro_model.tipo_cadastro,
        carteira=carteira,
    )

    return cadastro