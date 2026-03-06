# models/disease_model.py

from pydantic import BaseModel


class DiseaseReport(BaseModel):
    disease_name: str
    location: str
    cases: int


class DiseaseAnalytics(BaseModel):
    disease_name: str
    total_cases: int
    risk_level: str