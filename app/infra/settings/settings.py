from dataclasses import dataclass, field
from dynaconf import Dynaconf
from typing import List
from app.infra.interfaces.settings import SettingsInterface
from app.infra.utils.singleton import singleton
from app.infra.logger.logger import logger as lg


@singleton
@dataclass(slots=True, kw_only=True)
class SettingsManager(SettingsInterface):

    __envvar_prefix: str = "DYNACONF"
    __settings_files: List[str] = field(default_factory=lambda: ['settings.toml', '.secrets.toml', ".env"])
    __environments: bool = True
    __load_dotenv: bool = True
    __settings: Dynaconf | None = None
    
    def __create_settings(self) -> None:
        self.__settings = Dynaconf(
            envvar_prefix=self.__envvar_prefix,
            settings_files=self.__settings_files,
            environments=self.__environments,
            load_dotenv=self.__load_dotenv,
        )

    def __post_init__(self) -> None:
        self.__create_settings()

    def get_settings(self) -> Dynaconf:
        lg.info("Executando a função get_settings do SettingsManager")

        return self.__settings

settings: SettingsManager = SettingsManager()