from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmergencyRequest(BaseModel):
    name: str
    location: str
    issue: str


@router.post("/alert")
def send_emergency_alert(data: EmergencyRequest):

    return {
        "message": "Emergency alert sent",
        "patient": data.name,
        "location": data.location,
        "issue": data.issue
    }


@router.get("/status")
def emergency_status():
    return {"status": "Emergency system active"}