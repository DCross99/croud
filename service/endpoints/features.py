from fastapi import APIRouter, responses, Request

from service.models.api import Feature

router = APIRouter()


@router.post("/feature")
def feature(request: Request, payload: Feature) -> responses.JSONResponse:
    return responses.JSONResponse(status_code=200, content=payload.data)
