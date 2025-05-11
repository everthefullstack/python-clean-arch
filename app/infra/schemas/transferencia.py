from pydantic import BaseModel, Field


class TransferenciaSchemaRequest(BaseModel):
    pagador_id: int = Field(..., examples=[123])
    recebedor_id: int = Field(..., examples=[123])
    valor: float = Field(..., examples=[123.45])

