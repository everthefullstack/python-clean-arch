import logging as lg
from dataclasses import dataclass
from typing import Any
from sqlmodel import Session
from sqlalchemy.engine import Engine
from contextlib import contextmanager
from app.infra.interfaces.session import SessionInterface


@dataclass(slots=True, kw_only=True)
class SessionManager(SessionInterface):
    
    engine: Engine
    __session: Session | None = None

    def __create_session(self) -> None:
        self.__session = Session(self.engine.get_engine())
        lg.info("Session criada")
    
    def __post_init__(self) -> None:
        self.__create_session()

    @contextmanager
    def get_session(self, commit: bool = True) -> Any:
        try:
            lg.info("Session sendo enviada")
            yield self.__session

            lg.info("Session retornada")
            if commit:
                self.__session.commit()
                lg.info("Session commitada")

        except Exception as e:
            lg.info("Session rollbackada")
            self.__session.rollback()
            raise e

        finally:
            lg.info("Session encerrada")
            self.__session.close()
