from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SymptomRequest(BaseModel):
    symptom: str


@router.post("/predict")
def predict_symptom(data: SymptomRequest):

    symptom = data.symptom.lower()

    if "fever" in symptom or "cough" in symptom:
        return {
            "disease": "Possible Viral Infection",
            "risk": "Medium",
            "advice": "Drink fluids and rest"
        }

    elif "chest pain" in symptom:
        return {
            "disease": "Possible Heart Issue",
            "risk": "High",
            "advice": "Visit nearest hospital immediately"
        }

    elif "headache" in symptom:
        return {
            "disease": "Possible Migraine",
            "risk": "Low",
            "advice": "Drink water and rest"
        }

    else:
        return {
            "disease": "Unknown condition",
            "risk": "Unknown",
            "advice": "Consult a doctor"
        }