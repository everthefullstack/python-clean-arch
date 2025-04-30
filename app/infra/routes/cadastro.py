from fastapi import APIRouter, Request, HTTPException, Depends
from app.presentation.adapters.request import request_to_entity
from app.presentation.composers.cadastro_carteira_create import CadastroCarteiraCreateControllerComposer
from app.presentation.composers.cadastro_get import CadastroGetControllerComposer
from app.infra.schemas.cadastro import CadastroCarteiraSchemaRequest, CadastroGetSchemaRequest


cadastro_routes = APIRouter(tags=["Cadastro"], prefix="/cadastro")

@cadastro_routes.post("/")
async def cadastro_carteira_create(request: Request, req: CadastroCarteiraSchemaRequest):

    http_response = None

    try:
        controller = CadastroCarteiraCreateControllerComposer.compose()
        http_request = await request_to_entity(request=request)
        http_response = controller.cadastro_carteira_create(http_request=http_request)

        return http_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@cadastro_routes.get("/")
async def cadastro_get(request: Request, req: CadastroGetSchemaRequest = Depends()):
    
    http_response = None

    try:
        controller = CadastroGetControllerComposer.compose()
        http_request = await request_to_entity(request=request)
        http_response = controller.cadastro_get(http_request=http_request)

        return http_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
