from dataclasses import dataclass
from app.domain.entities.transferencia import Transferencia
from app.domain.entities.cadastro import Cadastro
from app.application.interfaces.transferencia import TransferenciaCreateUseCaseInterface
from app.infra.interfaces.transferencia_val_ext import TransferenciaValExtInterface
from app.infra.interfaces.transferencia_not_ext import TransferenciaNotExtInterface
from app.infra.interfaces.unit_of_work import UnitOfWorInterface
from app.infra.interfaces.logger import LoggerInterface


@dataclass(slots=True, kw_only=True)
class TransferenciaCreateUseCase(TransferenciaCreateUseCaseInterface):
    
    transferencia_create_uow: UnitOfWorInterface
    transferencia_val_ext: TransferenciaValExtInterface
    transferencia_not_ext: TransferenciaNotExtInterface
    transferencia_logger: LoggerInterface

    def transferencia_create(self, transferencia: Transferencia) -> Transferencia:
        self.transferencia_logger.info("Executando a função transferencia_create do caso de uso TransferenciaCreateUseCase")

        with self.transferencia_create_uow as uow:
            pagador: Cadastro = uow.cadastro_repository.select_cadastro(transferencia.pagador_id)
            recebedor: Cadastro = uow.cadastro_repository.select_cadastro(transferencia.recebedor_id)
            
            self.__validar_igualdade_pagador_e_recebedor(pagador, recebedor)
            self.__validar_faz_transferencia(pagador)
            self.__validar_saldo(pagador, transferencia.valor)
            self.__validar_transferencia_externa()
            pagador, recebedor = self.__atualizar_saldos(pagador, recebedor, transferencia.valor)

            uow.carteira_repository.update_saldo(pagador.carteira)
            uow.carteira_repository.update_saldo(recebedor.carteira)

            transferencia = uow.transferencia_repository.insert_transferencia(transferencia)

            self.__notificar_transferencia()

            return transferencia

    def __validar_igualdade_pagador_e_recebedor(self, pagador: Cadastro, recebedor: Cadastro):
        self.transferencia_logger.info("Executando a função __validar_igualdade_pagador_e_recebedor")

        if pagador.id == recebedor.id:
            raise ValueError("Pagador e recebedor não podem ser o mesmo.")

    def __validar_faz_transferencia(self, pagador: Cadastro):
        self.transferencia_logger.info("Executando a função __validar_faz_transferencia")

        if not pagador.faz_transferencia():
            raise ValueError("Não pode fazer transferência.")
        
    def __validar_saldo(self, pagador: Cadastro, valor: float):
        self.transferencia_logger.info("Executando a função __validar_saldo")

        if not pagador.carteira.tem_saldo(valor):
            raise ValueError("Saldo insuficiente para transferência.")

    def __validar_transferencia_externa(self):
        self.transferencia_logger.info("Executando a função __validar_transferencia_externa")

        if not self.transferencia_val_ext.validar_transferencia():
            raise ValueError("Transferência não autorizada pelo serviço externo.")
        
    def __atualizar_saldos(self, pagador: Cadastro, recebedor: Cadastro, valor: float):
        self.transferencia_logger.info("Executando a função __atualizar_saldos")

        pagador.carteira.saldo -= valor
        recebedor.carteira.saldo += valor
        return pagador, recebedor
    
    def __notificar_transferencia(self):
        self.transferencia_logger.info("Executando a função __notificar_transferencia")
        
        if not self.transferencia_not_ext.notificar_transferencia():
            self.transferencia_logger.error("Serviço de notificação de transferência não indisponível.")