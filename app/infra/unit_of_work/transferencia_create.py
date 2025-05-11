from dataclasses import dataclass
from app.infra.interfaces.session import SessionInterface
from app.infra.interfaces.unit_of_work import UnitOfWorInterface
from app.application.interfaces.cadastro import CadastroRepositoryInterface
from app.application.interfaces.carteira import CarteiraRepositoryInterface
from app.application.interfaces.transferencia import TransferenciaRepositoryInterface
from app.infra.logger.logger import logger as lg


@dataclass(slots=True)
class TransferenciaCreateUnitOfWork(UnitOfWorInterface):

    session: SessionInterface
    cadastro_repository: CadastroRepositoryInterface
    carteira_repository: CarteiraRepositoryInterface
    transferencia_repository: TransferenciaRepositoryInterface

    def __enter__(self) -> "TransferenciaCreateUnitOfWork":
        lg.info("Iniciando sessão.")
        self.cadastro_repository.session = self.session
        self.carteira_repository.session = self.session
        self.transferencia_repository.session = self.session
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            lg.info("Transação comittada com sucesso.")
            self.session.commit()

        else:
            lg.error(f"Error: {exc_type}, {exc_val}, {exc_tb}")
            lg.error("Transação desfeita devido ao erro")
            self.session.rollback()
            
        lg.info("Sessão fechada.")
        self.session.close()

    