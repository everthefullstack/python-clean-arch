from fastapi import APIRouter, Request, HTTPException, Depends
from app.presentation.adapters.request import request_to_entity
from app.presentation.composers.cadastro_carteira_create import CadastroCarteiraCreateControllerComposer
from app.presentation.composers.cadastro_get import CadastroGetControllerComposer
from app.infra.schemas.cadastro import CadastroCarteiraSchemaRequest, CadastroGetSchemaRequest
from app.infra.logger.logger import logger as lg


cadastro_routes = APIRouter(tags=["Cadastro"], prefix="/cadastro")

@cadastro_routes.post("/", status_code=201)   
async def cadastro_carteira_create(request: Request, req: CadastroCarteiraSchemaRequest):
    lg.info("Executando a função cadastro_carteira_create do cadastro_routes")

    http_response = None

    try:
        controller = CadastroCarteiraCreateControllerComposer.compose()
        http_request = await request_to_entity(request=request)
        http_response = controller.cadastro_carteira_create(http_request=http_request)

        return http_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@cadastro_routes.get("/", status_code=200)
async def cadastro_get(request: Request, req: CadastroGetSchemaRequest = Depends()):
    lg.info("Executando a função cadastro_get do cadastro_routes")
    
    http_response = None

    try:
        controller = CadastroGetControllerComposer.compose()
        http_request = await request_to_entity(request=request)
        http_response = controller.cadastro_get(http_request=http_request)

        return http_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
