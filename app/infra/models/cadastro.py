from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


class CadastroModel(SQLModel, table=True):
    __tablename__ = "cadastro"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    documento: str = Field(nullable=False, unique=True)
    email: str = Field(nullable=False, unique=True)
    senha: str = Field(nullable=False)
    tipo_cadastro: str = Field(default="u", nullable=False)
    carteira: Optional["CarteiraModel"] = Relationship(back_populates="cadastro")
    