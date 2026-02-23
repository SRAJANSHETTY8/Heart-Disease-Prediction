from pydantic import BaseModel, Field


class HeartDiseaseInput(BaseModel):
    age: float = Field(..., example=52)
    sex: int = Field(..., example=1, description="0 = Female, 1 = Male")
    cp: int = Field(..., example=0, description="Chest Pain Type")
    trestbps: float = Field(..., example=125)
    chol: float = Field(..., example=212)
    fbs: int = Field(..., example=0, description="Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)")
    restecg: int = Field(..., example=1)
    thalach: float = Field(..., example=168)
    exang: int = Field(..., example=0, description="Exercise Induced Angina")
    oldpeak: float = Field(..., example=1.0)
    slope: int = Field(..., example=2)
    ca: int = Field(..., example=0)
    thal: int = Field(..., example=2)