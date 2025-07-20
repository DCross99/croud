import base64
import json
from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime
from typing import Annotated, Literal


class Payload(BaseModel):
    url: str
    domain: Literal["youtube"] = Field(
        description="The domains that have been enabled for the scraper"
    )


def _pubsub_payload_to_dict(payload: str) -> dict:
    decoded = base64.b64decode(payload.encode()).decode()
    return json.loads(decoded)


class PubSubEnvelope(BaseModel):
    data: Annotated[Payload, BeforeValidator(_pubsub_payload_to_dict)]
    messageId: str
    publishTime: datetime


class PubSubSubscriptionEnvelope(BaseModel):
    # The class can be found in the docs here: https://cloud.google.com/pubsub/docs/push#receive_push
    message: PubSubEnvelope
    subscription: str
    deliveryAttempt: int
