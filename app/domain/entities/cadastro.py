from dataclasses import dataclass, asdict
from app.domain.interfaces.cadastro import CadastroAbc
from app.domain.entities.carteira import CarteiraAbc


@dataclass(slots=True, kw_only=True)
class Cadastro(CadastroAbc):
    
    tipo_cadastro: str | None = None
    carteira: CarteiraAbc | None = None

    def valida_documento(self) -> None:
        if len(self.documento) == 11:
            self.tipo_cadastro = "u"
        
        if len(self.documento) == 14:
            self.tipo_cadastro = "l"

    def faz_transferencia(self) -> bool:
        if self.tipo_cadastro == "u":
            return True
        
        return False
