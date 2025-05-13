from fastapi import FastAPI
from app.create_app import create_minimal_app
import pytest


@pytest.mark.asyncio
async def test_create_app():
    
    app = create_minimal_app()
    assert isinstance(app, FastAPI)