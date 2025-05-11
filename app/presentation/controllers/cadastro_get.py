from dataclasses import dataclass
from app.application.interfaces.cadastro import CadastroGetUseCaseInterface
from app.domain.entities.http_request import HttpRequest
from app.domain.entities.http_response import HttpResponse
from app.infra.logger.logger import logger as lg


@dataclass(slots=True)
class CadastroGetController:
    
    use_case: CadastroGetUseCaseInterface

    def cadastro_get(self, http_request: HttpRequest) -> HttpResponse:
        lg.info("Executando a função cadastro_get do CadastroGetController")
        
        id = http_request.query_params.get("id")
        response = self.use_case.cadastro_get(id=id)
        return HttpResponse(status_code=200, body={"data": response})
