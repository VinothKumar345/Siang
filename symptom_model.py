# models/symptom_model.py

from pydantic import BaseModel


class SymptomInput(BaseModel):
    symptom: str


class SymptomPrediction(BaseModel):
    disease: str
    risk_level: str
    advice: str