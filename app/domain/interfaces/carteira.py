from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional


#classe abstrata
@dataclass(slots=True, kw_only=True)
class CarteiraAbc(ABC):

    id: Optional[int] = field(default=None)
    saldo: float = field(default=100.0)
    cadastro_id: Optional[int] = field(default=None)
    
    @abstractmethod
    def tem_saldo(self, valor: float) -> bool:
        pass
