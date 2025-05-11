from dataclasses import dataclass
from app.domain.entities.cadastro import Cadastro
from app.application.interfaces.cadastro import CadastroGetUseCaseInterface, CadastroRepositoryInterface
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class CadastroGetUseCase(CadastroGetUseCaseInterface):

    cadastro_repository: CadastroRepositoryInterface

    def cadastro_get(self, id: int) -> Cadastro:
        lg.info("Executando a função cadastro_get do caso de uso CadastroGetUseCase")

        cadastro = self.cadastro_repository.select_cadastro(id=id)
        return cadastro
