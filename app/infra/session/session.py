from dataclasses import dataclass
from typing import Any
from sqlmodel import Session
from sqlalchemy.engine import Engine
from app.infra.interfaces.session import SessionInterface
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class SessionManager(SessionInterface):
    
    engine: Engine
    __session: Session | None = None

    def __create_session(self) -> None:
        self.__session = Session(self.engine.get_engine())
        
    def __post_init__(self) -> None:
        self.__create_session()

    def get_session(self) -> Any:
        lg.info("Executando a função get_session do SessionManager")
        return self.__session