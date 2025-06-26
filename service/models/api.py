from pydantic import BaseModel
from typing import Any
from datetime import datetime


class Feature(BaseModel):
    id: int
    timestamp: datetime
    data: dict[str, Any]
