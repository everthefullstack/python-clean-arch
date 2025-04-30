from dataclasses import dataclass
from app.domain.interfaces.carteira import CarteiraAbc


@dataclass(slots=True, kw_only=True)
class Carteira(CarteiraAbc):
    
    def tem_saldo(self, valor) -> bool:
        if (self.saldo - valor) > 0:
            return True
        
        return False
