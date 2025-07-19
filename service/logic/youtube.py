from fastapi import responses
from service.models import models
from service.logic.db import save_comments


def scrape_youtube(url: str) -> list[models.Comment]:
    # TODO: For the sake of the technical interview we will create
    # this dummy function so we are able to mock the return.
    return []


def youtube(url: str):
    analyzed_comments = scrape_youtube(url)
    save_comments(analyzed_comments)
    return responses.PlainTextResponse(
        status_code=200,
        content=f"Comments have been scraped and analyzed for {url=}",
    )
