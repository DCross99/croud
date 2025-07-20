import base64
import json
from typing import Any
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


def create_pubsub_envelope(
    payload: dict[str, Any],
    subscription: str = "pusbub-topic-name",
    envelope_attributes: dict | None = None,
) -> dict:
    """
    PubSub will send a message in the form of the wrapper below
    """
    return {
        "message": {
            "data": base64.b64encode(json.dumps(payload).encode()).decode(),
            "messageId": "1234",
            "publishTime": "2000-01-01T23:59:59Z",
            **(envelope_attributes or dict()),
        },
        "subscription": subscription,
        "deliveryAttempt": 1,
    }
