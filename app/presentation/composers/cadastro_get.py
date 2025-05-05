from dataclasses import dataclass
from app.infra.engine.engine import engine
from app.infra.session.session import SessionManager
from app.infra.repository.cadastro import CadastroRepository
from app.application.use_cases.cadastro_get import CadastroGetUseCase
from app.presentation.controllers.cadastro_get import CadastroGetController


@dataclass(slots=True, frozen=True)
class CadastroGetControllerComposer:

    @staticmethod
    def compose() -> CadastroGetController:
        
        session = SessionManager(engine=engine).get_session()
        repository = CadastroRepository(session=session)
        use_case = CadastroGetUseCase(cadastro_repository=repository)
        controller = CadastroGetController(use_case=use_case)

        return controller
