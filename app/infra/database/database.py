from dataclasses import dataclass
from sqlmodel import SQLModel
from app.infra.interfaces.database import DatabaseInterface
from app.infra.interfaces.engine import EngineInterface
from app.infra.models import *
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class DatabaseManager(DatabaseInterface):
    
    engine: EngineInterface

    def create_database(self) -> None:
        try:
            lg.info("Executando a função create_database do DatabaseManager")
            SQLModel.metadata.create_all(self.engine.get_engine())
        
        except Exception as e:
            lg.error(f"Erro ao criar o banco de dados: {e}")
            raise e
        