from dataclasses import dataclass
from app.domain.entities.cadastro import Cadastro
from app.application.interfaces.cadastro import CadastroGetUseCaseInterface, CadastroRepositoryInterface
from sqlmodel import Session


@dataclass(slots=True, kw_only=True)
class CadastroGetUseCase(CadastroGetUseCaseInterface):

    cadastro_repository: CadastroRepositoryInterface

    def cadastro_get(self, id: int, session: Session) -> Cadastro:
        cadastro = self.cadastro_repository.select_cadastro(id=id, session=session)
        return cadastro
