from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class TransferenciaModel(SQLModel, table=True):
    __tablename__ = "transferencia"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    valor: float = Field(nullable=False)
    pagador_id: int = Field(foreign_key="cadastro.id", nullable=False)
    recebedor_id: int = Field(foreign_key="cadastro.id", nullable=False)
    data: datetime = Field(default_factory=datetime.now)
