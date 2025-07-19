import uuid
from datetime import datetime


from service.models import models
from unittest import mock

from tests.integration.conftest import create_pubsub_envelope


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

    payload = {"url": "example.com", "domain": "youtube"}
    envelope = create_pubsub_envelope(payload)
    response = call_scraper(envelope)
    assert response.status_code == 200
    assert (
        response.text == "Comments have been scraped and analyzed for url='example.com'"
    )


def test_unconfigured_domain_raises_error(call_scraper):
    payload = {
        "url": "https://www.youtube.com/",
        "domain": "random_domain",
    }
    response = call_scraper(create_pubsub_envelope(payload))
    assert response.status_code == 422
