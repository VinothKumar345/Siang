from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class PregnancyRequest(BaseModel):
    start_date: str


@router.post("/status")
def pregnancy_status(data: PregnancyRequest):

    start = datetime.strptime(data.start_date, "%Y-%m-%d")
    today = datetime.today()

    diff = today - start

    weeks = diff.days // 7

    if weeks < 12:
        stage = "First Trimester"
    elif weeks < 28:
        stage = "Second Trimester"
    else:
        stage = "Third Trimester"

    return {
        "weeks": weeks,
        "stage": stage,
        "advice": "Maintain nutrition and attend regular checkups"
    }