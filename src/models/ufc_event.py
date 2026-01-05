from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, validator


class UfcEvent(BaseModel):
    fighters: str
    date: datetime

    @validator("fighters")
    def strip_fighters(cls, v: str) -> str:
        return v.strip()

    class Config:
        frozen = True
