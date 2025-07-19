# Croud Technical Task

An API that will scrape a given URL for the comments left and analyse them for the sentiment score.

In short the sentiment analyzer is working and will run automatically on any new comment classes created.

The scraper and saving to the database is yet to be set-up.


## Installation

### Local
1. Install UV via the [docs](https://docs.astral.sh/uv/getting-started/installation/).
2. Check UV is installed by running 
```bash
uv
```
3. Install packages 
```bash
uv sync
```
4. Download required LLM model via 
```bash
uv run spacy download en_core_web_sm
```

### Docker

```bash
docker compose up
```


## Tests

Tests can either be run locally or via docker image

### Local
```bash
uv run pytest tests
```

### Docker
```bash
docker compose up
```
```bash
docker exec croud-api uv run pytest tests
```


## Gotchas

When running `uv sync` it will remove any downloaded packages that are not a part of `pyproject.toml`

You can either redownload the package each time or run `uv sync --inexact` which will prevent uv from cleaning unknown packages.
