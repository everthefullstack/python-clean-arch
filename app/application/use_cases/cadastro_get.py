from dataclasses import dataclass
from app.domain.entities.cadastro import Cadastro
from app.application.interfaces.cadastro import CadastroGetUseCaseInterface, CadastroRepositoryInterface
from app.infra.interfaces.logger import LoggerInterface


@dataclass(slots=True, kw_only=True)
class CadastroGetUseCase(CadastroGetUseCaseInterface):

    cadastro_repository: CadastroRepositoryInterface
    cadastro_logger: LoggerInterface

    def cadastro_get(self, id: int) -> Cadastro:
        self.cadastro_logger.info("Executando a função cadastro_get do caso de uso CadastroGetUseCase")

        cadastro = self.cadastro_repository.select_cadastro(id=id)
        return cadastro
