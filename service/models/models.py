from typing import Literal
from pydantic import BaseModel, Field, computed_field
from datetime import datetime

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob  # noqa: F401

model = spacy.load("en_core_web_sm")
model.add_pipe("spacytextblob")


class Comment(BaseModel):
    id: str
    text: str = Field(description="Raw text of comment")
    likes: int = Field(
        description="Number of thumbs ups that have been given to the comment"
    )
    dislikes: int = Field(
        description="Number of thumbs downs that have been given to the comment"
    )
    parent_id: str = Field(description="The id of the comment that it is in reply of")
    posted_timestamp: datetime

    @computed_field()
    @property
    def score(self) -> float:
        # This method is called when the class is initiated
        self._doc = model(self.text)
        return self._doc._.blob.polarity

    @computed_field()
    @property
    def label(self) -> Literal["Negative", "Neutral", "Positive"]:
        # This method is called when the class is initiated
        if self.score > 0:
            return "Positive"
        elif self.score < 0:
            return "Negative"
        else:
            return "Neutral"
