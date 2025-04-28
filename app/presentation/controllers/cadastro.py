from dataclasses import dataclass
from app.application.interfaces.cadastro import CadastroUseCaseInterface
from app.domain.entities.http_request import HttpRequest
from app.domain.entities.http_response import HttpResponse
from app.domain.entities.cadastro import Cadastro


@dataclass(slots=True)
class CadastroController:
    use_case: CadastroUseCaseInterface

    def create_cadastro(self, http_request: HttpRequest) -> HttpResponse:
        cadastro = Cadastro(nome=http_request.body.get("nome"),
                            documento=http_request.body.get("documento"),
                            email=http_request.body.get("email"),
                            senha=http_request.body.get("senha"))

        response = self.use_case.create_cadastro(cadastro=cadastro)
        return HttpResponse(status_code=200, body={"data": response})

    def get_cadastro(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.body.get("id")

        response = self.use_case.get_cadastro(id=id)
        return HttpResponse(status_code=200, body={"data": response})