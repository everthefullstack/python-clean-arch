from pydantic import BaseModel, Field, EmailStr


class CadastroSchemaRequest(BaseModel):
    nome: str = Field(..., examples=["João Silva", "Maria Oliveira"])
    documento: str = Field(..., examples=["12345678900"])
    email: EmailStr = Field(..., examples=["joao@email.com"])
    senha: str = Field(..., examples=["MinhaSenha123"])
