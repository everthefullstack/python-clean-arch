from pydantic import BaseModel, Field, EmailStr


class CadastroCarteiraSchemaRequest(BaseModel):
    nome: str = Field(..., examples=["João Silva", "Maria Oliveira"])
    documento: str = Field(..., examples=["12345678900"])
    email: EmailStr = Field(..., examples=["joao@email.com"])
    senha: str = Field(..., examples=["MinhaSenha123"])

class CadastroGetSchemaRequest(BaseModel):
    id: int = Field(..., gt=0, examples=[1, 2, 3])
