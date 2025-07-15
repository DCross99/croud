from fastapi import APIRouter, responses

router = APIRouter()


@router.get("/health")
def health() -> responses.JSONResponse:
    return responses.JSONResponse(status_code=200, content="healthy")
