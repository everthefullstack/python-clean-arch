from dataclasses import dataclass
from app.infra.engine.engine import engine
from app.infra.session.session import SessionManager
from app.infra.repository.transferencia import TransferenciaRepository
from app.infra.repository.cadastro import CadastroRepository
from app.infra.repository.carteira import CarteiraRepository
from app.application.use_cases.transferencia_create import TransferenciaCreateUseCase
from app.presentation.controllers.transferencia_create import TransferenciaCreateController
from app.infra.unit_of_work.transferencia_create import TransferenciaCreateUnitOfWork
from app.infra.services.transferencia_val_ext import TransferenciaValExtService
from app.infra.services.transferencia_not_ext import TransferenciaNotExtService
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, frozen=True)
class TransferenciaCreateControllerComposer:

    @staticmethod
    def compose() -> TransferenciaCreateController:
        lg.info("Executando a função compose do TransferenciaCreateControllerComposer")
        
        session = SessionManager(engine=engine).get_session()
        cadastro_repository = CadastroRepository()
        carteira_repository = CarteiraRepository()
        transferencia_repository = TransferenciaRepository()
        transferencia_val_ext = TransferenciaValExtService()
        transferencia_not_ext = TransferenciaNotExtService()
        logger = lg
        transferencia_create_uow = (TransferenciaCreateUnitOfWork(
            session=session,
            cadastro_repository=cadastro_repository,
            carteira_repository=carteira_repository,
            transferencia_repository=transferencia_repository)
        )
        
        transferencia_create_use_case = TransferenciaCreateUseCase(
            transferencia_create_uow=transferencia_create_uow,
            transferencia_val_ext=transferencia_val_ext,
            transferencia_not_ext=transferencia_not_ext,
            transferencia_logger=logger
        )

        controller = TransferenciaCreateController(
            transferencia_create_use_case=transferencia_create_use_case
        )
        
        return controller
