import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.create_app import create_minimal_app


@pytest_asyncio.fixture(scope="function")
async def http_client():
    async with AsyncClient(
        transport=ASGITransport(app=create_minimal_app()), 
        base_url="http://127.0.0.1:8000/"
    ) as client:
        yield client
