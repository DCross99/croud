from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


class Payload(BaseModel):
    url: str
    domain: Literal["youtube"] = Field(
        description="The domains that have been enabled for the scraper"
    )
    timestamp: datetime
