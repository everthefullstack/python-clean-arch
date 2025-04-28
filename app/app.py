from fastapi import FastAPI
from app.presentation.composers.database import create_database
from app.infra.routes.cadastro import cadastro_routes


def create_app():

    create_database()
    
    app: FastAPI = FastAPI()
    app.include_router(cadastro_routes)
    

    return app