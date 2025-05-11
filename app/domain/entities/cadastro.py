from dataclasses import dataclass, asdict
from app.domain.interfaces.cadastro import CadastroAbc
from app.domain.entities.carteira import Carteira


@dataclass(slots=True, kw_only=True)
class Cadastro(CadastroAbc):
    
    tipo_cadastro: str | None = None # Tipo de cadastro: "c" para comum, "l" para lojista
    carteira: Carteira | None = None

    def valida_documento(self) -> None:
        if len(self.documento) not in [11, 14]:
            raise ValueError("Documento inválido. Deve ter 11 ou 14 dígitos.")
        
        if len(self.documento) == 11:
            self.tipo_cadastro = "c"
        
        if len(self.documento) == 14:
            self.tipo_cadastro = "l"

    def faz_transferencia(self) -> bool:
        if self.tipo_cadastro == "c":
            return True
        
        return False
