FROM python:3.12-slim-bookworm AS base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

### base ###

FROM base AS uv

WORKDIR /build/

COPY uv.lock pyproject.toml ./ 

# By running UV sync before we copy any files means we can cache the image
RUN uv sync --frozen --no-dev
RUN uv run spacy download en_core_web_sm 

### dev ###
FROM uv AS dev
ENV PYTHONPATH /build

RUN uv sync --frozen
RUN uv run spacy download en_core_web_sm

COPY service ./service
COPY tests ./tests

CMD uv run --no-dev --frozen uvicorn service.app:app --reload --reload-dir service --host 0.0.0.0 --port $PORT

### app ###

FROM uv AS app
ENV PYTHONPATH /build

COPY service ./service

CMD uv run --no-dev --frozen uvicorn service.app:app --reload --reload-dir service --host 0.0.0.0 --port $PORT
