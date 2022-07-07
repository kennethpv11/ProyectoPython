from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Measure(BaseModel):
    id: Optional[int]
    device: str
    measure: str
    magnitude: float
    timestamp: datetime
