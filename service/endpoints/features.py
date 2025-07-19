from fastapi import APIRouter, responses, Request, HTTPException

from service.models.api import Payload
from service.logic.youtube import youtube

router = APIRouter()


@router.post("/scraper")
def scraper(request: Request, payload: Payload) -> responses.PlainTextResponse:
    match payload.domain:
        case "youtube":
            return youtube(payload.url)
        case _:
            raise HTTPException(status_code=404, detail="Item not found")
