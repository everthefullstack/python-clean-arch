from dataclasses import dataclass
from app.infra.engine.engine import engine
from app.infra.session.session import SessionManager
from app.infra.repository.cadastro import CadastroRepository
from app.infra.repository.carteira import CarteiraRepository
from app.application.use_cases.cadastro_carteira_create import CadastroCarteiraCreateUseCase
from app.presentation.controllers.cadastro_carteira import CadastroCarteiraCreateController
from app.infra.unit_of_work.cadastro_carteira_create import CadastroCarteiraCreateUnitOfWork
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, frozen=True)
class CadastroCarteiraCreateControllerComposer:

    @staticmethod
    def compose() -> CadastroCarteiraCreateController:
        lg.info("Executando a função compose do CadastroCarteiraCreateControllerComposer")
        
        session = SessionManager(engine=engine).get_session()
        cadastro_repository = CadastroRepository()
        carteira_repository = CarteiraRepository()
        logger = lg
        cadastro_carteira_uow = (CadastroCarteiraCreateUnitOfWork(
            session=session,
            cadastro_repository=cadastro_repository,
            carteira_repository=carteira_repository)
        )
        
        cadastro_carteira_use_case = CadastroCarteiraCreateUseCase(
            cadastro_carteira_create_uow=cadastro_carteira_uow,
            cadastro_carteira_logger=logger
        )
        controller = CadastroCarteiraCreateController(
            cadastro_carteira_create_use_case=cadastro_carteira_use_case
        )
        return controller
