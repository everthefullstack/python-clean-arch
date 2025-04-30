from sqlmodel import Field, SQLModel, Relationship
from typing import Optional


class CarteiraModel(SQLModel, table=True):
    __tablename__ = "carteira"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    saldo: float = Field(default=0.0, nullable=False)
    cadastro_id: int = Field(foreign_key="cadastro.id", nullable=False, unique=True)
    cadastro: Optional["CadastroModel"] = Relationship(back_populates="carteira")