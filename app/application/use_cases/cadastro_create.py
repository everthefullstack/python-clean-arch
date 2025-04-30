from dataclasses import dataclass
from app.domain.entities.cadastro import Cadastro
from app.application.interfaces.cadastro import CadastroCreateUseCaseInterface, CadastroRepositoryInterface
from sqlmodel import Session


@dataclass(slots=True, kw_only=True)
class CadastroCreateUseCase(CadastroCreateUseCaseInterface):

    cadastro_repository: CadastroRepositoryInterface

    def cadastro_create(self, cadastro: Cadastro, session: Session):
        cadastro.valida_documento()
        cadastro = self.cadastro_repository.insert_cadastro(cadastro=cadastro, session=session)
        return cadastro
