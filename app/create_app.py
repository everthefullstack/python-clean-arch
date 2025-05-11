from fastapi import FastAPI
from app.presentation.composers.database import create_database
from app.infra.routes.cadastro import cadastro_routes
from app.infra.routes.transferencia import transferencia_routes
from app.infra.logger.logger import logger as lg


def create_app():
    lg.info("Executando a função create_app")
    
    app: FastAPI = FastAPI()
    app.include_router(cadastro_routes)
    app.include_router(transferencia_routes)
    create_database()
    
    return app
