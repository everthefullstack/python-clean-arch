from dataclasses import dataclass
from sqlmodel import Session, select
from app.domain.entities.cadastro import Cadastro
from app.infra.models.cadastro import CadastroModel
from app.application.interfaces.cadastro import CadastroRepositoryInterface
from app.presentation.adapters.cadastro import entity_to_model, model_to_entity
from app.infra.logger.logger import logger as lg


@dataclass(slots=True, kw_only=True)
class CadastroRepository(CadastroRepositoryInterface):

    session: Session | None = None

    def insert_cadastro(self, cadastro: Cadastro) -> Cadastro:
        lg.info("Executando a função insert_cadastro do CadastroRepository")

        cadastro_model: CadastroModel = entity_to_model(cadastro)
        self.session.add(cadastro_model)
        self.session.flush()
        return model_to_entity(cadastro_model)
        
    def select_cadastro(self, id: int) -> Cadastro | None:
        lg.info("Executando a função select_cadastro do CadastroRepository")
        
        stmt = select(CadastroModel).where(CadastroModel.id == id)
        cadastro_model: CadastroModel | None = self.session.exec(statement=stmt).one_or_none()
        return model_to_entity(cadastro_model)
