from dataclasses import dataclass
from app.infra.settings.settings import settings
from app.infra.interfaces.transferencia_val_ext import TransferenciaValExtInterface
from httpx import Client, TimeoutException
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class TransferenciaValExtService(TransferenciaValExtInterface):

    __url: str | None = None

    def validar_transferencia(self) -> bool:
        lg.info("Executando a função validar_transferencia do TransferenciaValExtService")
        
        with Client() as client:
            try:
                self.__url = settings.get_settings().TRANSFER_AUTHORIZATION_URL
                response = client.get(url=self.__url, timeout=30).json()

                if response["status"] == "success" and response["data"]["authorization"] == True:
                    return True
                
                return False

            except TimeoutException:
                lg.error("Timeout ao acessar o serviço externo.")
                return False
            
            except Exception as e:
                lg.error(f"Erro ao acessar o serviço externo: {e}")
                return False
                