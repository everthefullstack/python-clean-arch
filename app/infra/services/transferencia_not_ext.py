from dataclasses import dataclass
from app.infra.settings.settings import settings
from app.infra.interfaces.transferencia_not_ext import TransferenciaNotExtInterface
from httpx import Client, TimeoutException
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class TransferenciaNotExtService(TransferenciaNotExtInterface):

    __url: str | None = None

    def notificar_transferencia(self) -> bool:
        lg.info("Executando a função notificar_transferencia do TransferenciaNotExtService")
        
        with Client() as client:
            try:
                self.__url = settings.get_settings().TRANSFER_NOTIFICATION_SEND_URL
                response = client.post(url=self.__url, timeout=30)

                if response.status_code == 204:
                    lg.info("Notificação de transferência enviada com sucesso.")
                    return True
                
                else:
                    lg.error(f"Falha ao enviar notificação de transferência: {response.status_code}")
                    return False

            except TimeoutException:
                lg.error("Timeout ao acessar o serviço externo.")
                return False
            
            except Exception as e:
                lg.error(f"Erro ao acessar o serviço externo: {e}")
                return False
                