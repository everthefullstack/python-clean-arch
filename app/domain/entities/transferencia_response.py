from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class TransferenciaData:
    
    authorization: bool

@dataclass(slots=True, kw_only=True)
class TransferenciaResponse:

    status: str
    data: TransferenciaData
    