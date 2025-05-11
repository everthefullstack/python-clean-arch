from dataclasses import dataclass
from app.application.interfaces.transferencia import TransferenciaCreateUseCaseInterface
from app.domain.entities.http_request import HttpRequest
from app.domain.entities.http_response import HttpResponse
from app.domain.entities.transferencia import Transferencia
from app.infra.logger.logger import logger as lg


@dataclass(slots=True)
class TransferenciaCreateController:
    
    transferencia_create_use_case: TransferenciaCreateUseCaseInterface

    def transferencia_create(self, http_request: HttpRequest) -> HttpResponse:
        lg.info("Executando a função transferencia_create do TransferenciaCreateController")
        
        transferencia = Transferencia(pagador_id=http_request.body.get("pagador_id"),
                                      recebedor_id=http_request.body.get("recebedor_id"),
                                      valor=http_request.body.get("valor"))

        transferencia = self.transferencia_create_use_case.transferencia_create(transferencia=transferencia)
        
        return HttpResponse(status_code=201, body={"data": transferencia})
