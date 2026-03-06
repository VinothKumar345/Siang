# models/pregnancy_model.py

from pydantic import BaseModel
from datetime import date


class PregnancyInput(BaseModel):
    mother_name: str
    age: int
    start_date: date


class PregnancyStatus(BaseModel):
    weeks: int
    stage: str
    advice: str