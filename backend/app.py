from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

from model_loader import load_model, load_scaler
from schema import HeartDiseaseInput


# Initialize FastAPI app
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease risk using Random Forest model",
    version="1.0.0"
)

# Allow frontend connection (important for Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and scaler once at startup
model = load_model()
scaler = load_scaler()


@app.get("/")
def health_check():
    return {
        "status": "API is running successfully",
        "model_loaded": True
    }


@app.post("/predict")
def predict(data: HeartDiseaseInput):
    try:
        # Convert input into numpy array
        input_data = np.array([[
            data.age,
            data.sex,
            data.cp,
            data.trestbps,
            data.chol,
            data.fbs,
            data.restecg,
            data.thalach,
            data.exang,
            data.oldpeak,
            data.slope,
            data.ca,
            data.thal
        ]])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        # Risk interpretation
        if prediction == 1:
            risk_level = "High Risk"
            interpretation = "The model indicates a high likelihood of heart disease. Medical consultation is strongly recommended."
        else:
            risk_level = "Low Risk"
            interpretation = "The model indicates a low likelihood of heart disease. Maintain a healthy lifestyle and regular check-ups."

        return {
            "prediction": int(prediction),
            "probability": round(float(probability) * 100, 2),
            "risk_level": risk_level,
            "interpretation": interpretation
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")