from fastapi import Request
from app.domain.entities.http_request import HttpRequest
from app.infra.logger.logger import logger as lg


async def request_to_entity(request: Request) -> HttpRequest:
    lg.info("Executando a função request_to_entity do adaptador request")

    return HttpRequest(
        body=await request.json() if request.method in ["POST", "PUT", "PATCH"] else None,
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url,
        ipv4=request.client.host
    )