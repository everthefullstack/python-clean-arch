from httpx import AsyncClient
import pytest


url_prefix: str = "/cadastro/"

@pytest.mark.asyncio
async def test_create_cadastro_with_full_fields(http_client: AsyncClient):

    payload = {
        "nome": "João Silva",
        "documento": "12345678900",
        "email": "joaosilva@teste.com",
        "senha": "teste123"
    }

    response = await http_client.post(f"{url_prefix}", json=payload)
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_create_cadastro_without_nome(http_client: AsyncClient):

    payload = {
        "documento": "12345678900",
        "email": "joaosilva@teste.com",
        "senha": "teste123"
    }

    response = await http_client.post(f"{url_prefix}", json=payload)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_cadastro_with_full_fields_duplicated(http_client: AsyncClient):

    payload = {
        "nome": "João Silva",
        "documento": "12345678900",
        "email": "joaosilva@teste.com",
        "senha": "teste123"
    }

    response = await http_client.post(f"{url_prefix}", json=payload)
    assert response.status_code == 500

@pytest.mark.asyncio
async def test_get_cadastro(http_client: AsyncClient):
    id = 1
    response = await http_client.get(f"{url_prefix}{id}")
    assert response.status_code == 200
