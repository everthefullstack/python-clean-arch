from dataclasses import dataclass
from app.application.interfaces.cadastro import CadastroGetUseCaseInterface
from app.domain.entities.http_request import HttpRequest
from app.domain.entities.http_response import HttpResponse
from app.infra.interfaces.session import SessionInterface


@dataclass(slots=True)
class CadastroGetController:
    
    use_case: CadastroGetUseCaseInterface
    session: SessionInterface

    def cadastro_get(self, http_request: HttpRequest) -> HttpResponse:
        with self.session.get_session(commit=False) as session:
            if not session:
                return HttpResponse(status_code=500, body={"error": "Session error"})
            
            id = http_request.query_params.get("id")

            response = self.use_case.cadastro_get(id=id, session=session)
            return HttpResponse(status_code=200, body={"data": response})
