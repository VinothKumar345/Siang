from fastapi import APIRouter

router = APIRouter()

hospitals = [
    {"name": "Rural Health Clinic", "distance": "2 km"},
    {"name": "Government Hospital", "distance": "4 km"},
    {"name": "City Medical Center", "distance": "6 km"}
]


@router.get("/nearby")
def get_nearby_hospitals():
    return {"hospitals": hospitals}