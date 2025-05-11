from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Transferencia:

    id: Optional[int] = field(default=None)
    valor: float
    pagador_id: int
    recebedor_id: int
    data: datetime = field(default_factory=datetime.now)
