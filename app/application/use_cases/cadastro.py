from dataclasses import dataclass
from app.domain.entities.cadastro import Cadastro
from app.application.interfaces.cadastro import CadastroUseCaseInterface, CadastroRepositoryInterface


@dataclass(slots=True, kw_only=True)
class CadastroUseCase(CadastroUseCaseInterface):

    cadastro_repository: CadastroRepositoryInterface

    def create_cadastro(self, cadastro: Cadastro):
        cadastro = self.cadastro_repository.insert_cadastro(cadastro=cadastro)
        return cadastro
    
    def get_cadastro(self, id: int) -> Cadastro:
        cadastro = self.cadastro_repository.select_cadastro(id=id)
        return cadastro
