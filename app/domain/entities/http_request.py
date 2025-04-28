from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class HttpRequest:

    headers: dict | None = None
    body: dict | None = None
    query_params: dict | None = None
    path_params: dict | None = None
    url: str | None = None
    ipv4: str | None = None