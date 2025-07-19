import uuid
from fastapi.encoders import jsonable_encoder
from datetime import datetime


from service.models import models
from service.models.api import Payload
from unittest import mock


@mock.patch("service.logic.youtube.scrape_youtube")
def test_example_style_of_integration_test(mock_scrape_youtube, call_scraper):
    mock_scrape_youtube.return_value = [
        models.Comment(
            id=str(uuid.uuid4()),
            text="I have no feelings",
            likes=10,
            dislikes=0,
            parent_id=str(uuid.uuid4()),
            posted_timestamp=datetime.now(),
        )
    ]
    payload = jsonable_encoder(
        Payload(url="example.com", domain="youtube", timestamp=datetime.now())
    )

    response = call_scraper(payload)
    assert response.status_code == 200
    assert (
        response.text == "Comments have been scraped and analyzed for url='example.com'"
    )


def test_unconfigured_domain_raises_error(call_scraper):
    payload = {
        "url": "https://www.youtube.com/",
        "domain": "random_domain",
        "timestamp": str(datetime.now()),
    }
    response = call_scraper(payload)
    assert response.status_code == 422
