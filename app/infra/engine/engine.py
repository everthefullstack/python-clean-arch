from dataclasses import dataclass, field
from sqlmodel import create_engine
from sqlalchemy.engine import Engine
from app.infra.settings.settings import settings
from app.infra.interfaces.settings import SettingsInterface
from app.infra.interfaces.engine import EngineInterface
from app.infra.utils.singleton import singleton
from app.infra.logger.logger import logger as lg


@singleton
@dataclass(slots=True, kw_only=True)
class EngineManager(EngineInterface):
    
    __engine: Engine = field(repr=False, init=False)
    settings: SettingsInterface

    def __create_engine(self) -> None:
        url: str = self.settings.get_settings().DATABASE_URL
        self.__engine = create_engine(url=url, echo=True)

    def __post_init__(self) -> None:
        self.__create_engine()

    def get_engine(self) -> None:
        lg.info("Executando a função get_engine do EngineManager")
        
        return self.__engine

engine: EngineManager = EngineManager(settings=settings)