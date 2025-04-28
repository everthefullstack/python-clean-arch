from dataclasses import dataclass
from sqlmodel import Session, select
from app.domain.entities.cadastro import Cadastro
from app.infra.models.cadastro import CadastroModel
from app.application.interfaces.cadastro import CadastroRepositoryInterface
from app.presentation.adapters.cadastro import entity_to_model, model_to_entity


@dataclass(slots=True, kw_only=True)
class CadastroRepository(CadastroRepositoryInterface):

    session: Session

    def insert_cadastro(self, cadastro: Cadastro) -> Cadastro:
        with self.session as session:
            cadastro_model: CadastroModel = entity_to_model(cadastro)
            session.add(cadastro_model)
            session.commit()
            session.refresh(cadastro_model)
            return model_to_entity(cadastro_model)
        
    def select_cadastro(self, id: int) -> Cadastro | None:
        with self.session as session:
            query = select(CadastroModel).where(CadastroModel.id == id)
            cadastro_model: CadastroModel | None = session.scalar(statement=query)
            return model_to_entity(cadastro_model)
