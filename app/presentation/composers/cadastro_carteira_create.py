from dataclasses import dataclass
from app.infra.engine.engine import engine
from app.infra.session.session import SessionManager
from app.infra.repository.cadastro import CadastroRepository
from app.infra.repository.carteira import CarteiraRepository
from app.application.use_cases.cadastro_create import CadastroCreateUseCase
from app.application.use_cases.carteira_create import CarteiraCreateUseCase
from app.presentation.controllers.cadastro_carteira import CadastroCarteiraCreateController


@dataclass(slots=True, frozen=True)
class CadastroCarteiraCreateControllerComposer:

    @staticmethod
    def compose() -> CadastroCarteiraCreateController:
        
        session: SessionManager = SessionManager(engine=engine)
        cadastro_repository: CadastroRepository = CadastroRepository()
        carteira_repository: CarteiraRepository = CarteiraRepository()
        cadastro_use_case: CadastroCreateUseCase = CadastroCreateUseCase(cadastro_repository=cadastro_repository)
        carteira_use_case: CarteiraCreateUseCase = CarteiraCreateUseCase(carteira_repository=carteira_repository)
        controller: CadastroCarteiraCreateController = CadastroCarteiraCreateController(cadastro_use_case=cadastro_use_case,
                                                                                        carteira_use_case=carteira_use_case,
                                                                                        session=session)
        return controller
