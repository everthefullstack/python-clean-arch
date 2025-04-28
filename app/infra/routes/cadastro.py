from fastapi import APIRouter, Request, HTTPException
from app.presentation.adapters.request import request_to_entity
from app.presentation.composers.cadastro import CadastroControllerComposer
from app.infra.schemas.cadastro import CadastroSchemaRequest


cadastro_routes = APIRouter(tags=["Cadastro"], prefix="/cadastro")


@cadastro_routes.post("/")
async def create_cadastro(req: CadastroSchemaRequest, request: Request):

    http_response = None

    try:
        controller = CadastroControllerComposer.compose()
        http_request = await request_to_entity(request=request)
        http_response = controller.create_cadastro(http_request=http_request)

        return http_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@cadastro_routes.get("/")
async def get_cadastro(req: int, request: Request):
    
    http_response = None

    try:
        controller = CadastroControllerComposer.compose()
        http_request = await request_to_entity(request=request)
        http_response = controller.get_cadastro(http_request=http_request)

        return http_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))