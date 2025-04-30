from dataclasses import dataclass
from app.application.interfaces.cadastro import CadastroCreateUseCaseInterface
from app.application.interfaces.carteira import CarteiraCreateUseCaseInterface
from app.domain.entities.http_request import HttpRequest
from app.domain.entities.http_response import HttpResponse
from app.domain.entities.cadastro import Cadastro
from app.domain.entities.carteira import Carteira
from app.infra.interfaces.session import SessionInterface


@dataclass(slots=True)
class CadastroCarteiraCreateController:
    
    cadastro_use_case: CadastroCreateUseCaseInterface
    carteira_use_case: CarteiraCreateUseCaseInterface
    session: SessionInterface
    
    def cadastro_carteira_create(self, http_request: HttpRequest) -> HttpResponse:
        
        with self.session.get_session() as session:
            if not session:
                return HttpResponse(status_code=500, body={"error": "Session error"})
            
            cadastro = Cadastro(nome=http_request.body.get("nome"),
                                documento=http_request.body.get("documento"),
                                email=http_request.body.get("email"),
                                senha=http_request.body.get("senha"))
            cadastro = self.cadastro_use_case.cadastro_create(cadastro=cadastro, session=session)

            carteira = Carteira(cadastro_id=cadastro.id)
            carteira = self.carteira_use_case.carteira_create(carteira=carteira, session=session)
            
            return HttpResponse(status_code=201, body={"data": "ok"})
