from app.domain.entities.http_response import HttpResponse
from typing import Dict


def entity_to_response(status_code: int, body: Dict) -> HttpResponse:
    return HttpResponse(
        status_code=status_code,
        body=body,
    )