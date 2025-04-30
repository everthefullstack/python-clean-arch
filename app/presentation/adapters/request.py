from fastapi import Request
from app.domain.entities.http_request import HttpRequest


async def request_to_entity(request: Request) -> HttpRequest:
    return HttpRequest(
        body=await request.json() if request.method in ["POST", "PUT", "PATCH"] else None,
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url,
        ipv4=request.client.host
    )