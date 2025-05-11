from app.domain.entities.http_response import HttpResponse
from typing import Dict
from app.infra.logger.logger import logger as lg


def entity_to_response(status_code: int, body: Dict) -> HttpResponse:
    lg.info("Executando a função entity_to_response do adaptador de response")

    return HttpResponse(
        status_code=status_code,
        body=body,
    )