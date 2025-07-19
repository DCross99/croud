from fastapi import APIRouter, responses

from service.models.api import PubSubSubscriptionEnvelope, Payload
from service.logic.youtube import youtube

router = APIRouter()


@router.post("/scraper")
def scraper(
    subscription_message: PubSubSubscriptionEnvelope,
) -> responses.PlainTextResponse:
    payload: Payload = subscription_message.message.data
    match payload.domain:
        case "youtube":
            return youtube(payload.url)
