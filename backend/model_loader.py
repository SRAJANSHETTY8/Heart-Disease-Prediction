import os
import joblib

# Get the directory where model_loader.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct correct paths to model files
MODEL_PATH = os.path.join(BASE_DIR, "model", "heart_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
    
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")


def load_scaler():
    if not os.path.exists(SCALER_PATH):
        raise FileNotFoundError(f"Scaler file not found at: {SCALER_PATH}")
    
    try:
        scaler = joblib.load(SCALER_PATH)
        return scaler
    except Exception as e:
        raise RuntimeError(f"Error loading scaler: {e}")