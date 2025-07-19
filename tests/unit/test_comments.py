import uuid
from datetime import datetime

from service.models import models


def test_comment_executed_for_neutral_sentence():
    comment = models.Comment(
        id=str(uuid.uuid4()),
        text="I have no feelings",
        likes=10,
        dislikes=0,
        parent_id=str(uuid.uuid4()),
        posted_timestamp=datetime.now(),
    )

    assert comment.score == 0.0
    assert comment.label == "Neutral"


def test_comment_executed_for_positive_sentence():
    comment = models.Comment(
        id=str(uuid.uuid4()),
        text="Oh my I am so happy!!!",
        likes=10,
        dislikes=0,
        parent_id=str(uuid.uuid4()),
        posted_timestamp=datetime.now(),
    )

    assert comment.score > 0
    assert comment.label == "Positive"


def test_comment_executed_for_negative_sentence():
    comment = models.Comment(
        id=str(uuid.uuid4()),
        text="Oh my I am so angry!!!",
        likes=10,
        dislikes=0,
        parent_id=str(uuid.uuid4()),
        posted_timestamp=datetime.now(),
    )

    assert comment.score < 0
    assert comment.label == "Negative"
