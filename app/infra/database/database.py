import logging as lg
from dataclasses import dataclass
from sqlmodel import SQLModel
from app.infra.interfaces.database import DatabaseInterface
from app.infra.interfaces.engine import EngineInterface
from app.infra.models import *


@dataclass(slots=True, kw_only=True)
class DatabaseManager(DatabaseInterface):
    
    engine: EngineInterface

    def create_database(self) -> None:
        SQLModel.metadata.create_all(self.engine.get_engine())
        lg.info("Database criada")
