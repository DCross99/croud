from fastapi.testclient import TestClient
import pytest
from fastapi import FastAPI

from service.endpoints import features, probes


@pytest.fixture()
def call_scraper(client):
    def handler(message: dict):
        response = client.post("/scraper", json=message)
        return response

    return handler


@pytest.fixture()
def client():
    app = FastAPI()
    app.include_router(features.router)
    app.include_router(probes.router)

    with TestClient(app) as test_client:
        yield test_client
