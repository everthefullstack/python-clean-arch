from dataclasses import dataclass
from app.application.interfaces.cadastro_carteira import CadastroCarteiraCreateUseCaseInterface
from app.domain.entities.http_request import HttpRequest
from app.domain.entities.http_response import HttpResponse
from app.domain.entities.cadastro import Cadastro
from app.domain.entities.carteira import Carteira


@dataclass(slots=True)
class CadastroCarteiraCreateController:
    
    cadastro_carteira_create_use_case: CadastroCarteiraCreateUseCaseInterface

    def cadastro_carteira_create(self, http_request: HttpRequest) -> HttpResponse:
        
        cadastro = Cadastro(nome=http_request.body.get("nome"),
                            documento=http_request.body.get("documento"),
                            email=http_request.body.get("email"),
                            senha=http_request.body.get("senha"))
        
        carteira = Carteira()

        cadastro_carteira = self.cadastro_carteira_create_use_case.cadastro_carteira_create(cadastro=cadastro, 
                                                                                            carteira=carteira)
        
        return HttpResponse(status_code=201, body={"data": cadastro_carteira})
