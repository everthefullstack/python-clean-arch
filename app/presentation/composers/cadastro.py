from dataclasses import dataclass
from app.infra.engine.engine import engine
from app.infra.session.session import SessionManager
from app.infra.repository.cadastro import CadastroRepository
from app.application.use_cases.cadastro import CadastroUseCase
from app.presentation.controllers.cadastro import CadastroController


@dataclass(slots=True, frozen=True)
class CadastroControllerComposer:

    @staticmethod
    def compose() -> CadastroController:
        
        session: SessionManager = SessionManager(engine=engine).get_session()
        repository: CadastroRepository = CadastroRepository(session=session)
        use_case: CadastroUseCase = CadastroUseCase(cadastro_repository=repository)
        controller: CadastroController = CadastroController(use_case=use_case)

        return controller