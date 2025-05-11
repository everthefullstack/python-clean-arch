from fastapi import APIRouter, Request, HTTPException
from app.presentation.adapters.request import request_to_entity
from app.presentation.composers.transferencia_create import TransferenciaCreateControllerComposer
from app.infra.schemas.transferencia import TransferenciaSchemaRequest
from app.infra.logger.logger import logger as lg


transferencia_routes = APIRouter(tags=["Transferencia"], prefix="/transferencia")

@transferencia_routes.post("/")
async def transferencia_create(request: Request, req: TransferenciaSchemaRequest):
    lg.info("Executando a função transferencia_create do transferencia_routes")
    
    http_response = None

    try:
        controller = TransferenciaCreateControllerComposer.compose()
        http_request = await request_to_entity(request=request)
        http_response = controller.transferencia_create(http_request=http_request)

        return http_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


