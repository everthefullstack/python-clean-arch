from dataclasses import dataclass
from app.domain.entities.cadastro import Cadastro
from app.domain.entities.carteira import Carteira
from app.application.interfaces.cadastro_carteira import CadastroCarteiraCreateUseCaseInterface
from app.infra.interfaces.unit_of_work import UnitOfWorInterface


@dataclass(slots=True, kw_only=True)
class CadastroCarteiraCreateUseCase(CadastroCarteiraCreateUseCaseInterface):

    cadastro_carteira_create_uow: UnitOfWorInterface

    def cadastro_carteira_create(self, cadastro: Cadastro, carteira: Carteira):
        
        with self.cadastro_carteira_create_uow as uow:
            cadastro.valida_documento()
            cadastro = uow.cadastro_repository.insert_cadastro(cadastro=cadastro)

            carteira.cadastro_id = cadastro.id
            carteira = uow.carteira_repository.insert_carteira(carteira=carteira)

            cadastro.carteira = carteira

            return cadastro
        