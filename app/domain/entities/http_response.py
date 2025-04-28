from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class HttpResponse:

    status_code: int
    body: dict