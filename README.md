# Heart Disease Prediction System

AI-powered clinical decision support system using Machine Learning and Web Application integration.

Heart Disease Prediction is a web-based application that uses machine learning to predict the likelihood of heart disease based on patient clinical and diagnostic parameters. The system allows users to enter medical information such as age, blood pressure, cholesterol levels, and other health indicators, and the model predicts whether the patient is at risk of heart disease.

---

## Overview

### Backend  
Python FastAPI server using a Random Forest classification model to predict heart disease risk.

### Frontend  
Streamlit-based user interface that allows users to input patient health parameters and view structured prediction results.

### Purpose  
Assist in early detection of heart disease risk using machine learning to support clinical decision-making and preventive healthcare strategies.

---

## Tech Stack

### Frontend
- Streamlit  
- Python  
- Requests  

### Backend
- Python  
- FastAPI  
- NumPy  
- Scikit-learn  
- Joblib  
- Pydantic  

### Machine Learning
- Model Used: Random Forest Classifier  
- Dataset: Heart Disease Dataset (400 records, 13 features + target)  

---

## Project Structure

backend/  
Contains FastAPI application and prediction API  

frontend/  
Contains Streamlit user interface code  

model/  
Contains trained machine learning model and scaler  

training/  
Contains training script and experimentation notebook  

dataset/  
Contains heart disease dataset used for training  

---

## Quick Start – Development Setup

Clone the repository

git clone https://github.com/SRAJANSHETTY8/Heart-Disease-Prediction.git  
cd Heart-Disease-Prediction  

Install dependencies

pip install -r backend/requirements.txt  
pip install -r frontend/requirements.txt  

---

## Run Backend Server

cd backend  
uvicorn app:app --reload  

Backend API will be available at:  
http://127.0.0.1:8000  

API documentation (Swagger UI):  
http://127.0.0.1:8000/docs  

---

## Run Frontend Application

cd frontend  
streamlit run streamlit_app.py  

Frontend will be available at:  
http://localhost:8501  

---

## How It Works

1. User enters patient clinical parameters such as age, blood pressure, cholesterol, and heart rate.  
2. The frontend sends input values to the backend prediction API.  
3. The backend loads the trained Random Forest model and scaler.  
4. Input values are preprocessed using the saved scaler.  
5. The model predicts whether heart disease risk is present (0 = No, 1 = Yes).  
6. The API returns structured output including:
   - Risk classification  
   - Probability percentage  
   - Clinical interpretation message  
7. Results are displayed clearly in the user interface.

---

## Dataset Information

The dataset contains 400 patient records with 13 clinical features including:

- Age  
- Sex  
- Chest Pain Type  
- Resting Blood Pressure  
- Cholesterol  
- Fasting Blood Sugar  
- Resting ECG  
- Maximum Heart Rate  
- Exercise Induced Angina  
- ST Depression  
- ST Slope  
- Number of Major Vessels  
- Thalassemia  

Target variable:  
0 = No Heart Disease  
1 = Heart Disease  

---

## Data Preprocessing

- Dataset contained no missing values.  
- All features were already in numerical format.  
- Feature scaling applied using StandardScaler.  
- Dataset split into 80% training and 20% testing.  
- Model evaluated using Accuracy, Precision, Recall, F1-score, and ROC-AUC.  

---

## Model Training

A Random Forest Classifier was used to train the model.  

The model was tuned with balanced class weights to improve medical risk detection.  

After training:
- The trained model was saved as a .pkl file.  
- The scaler was saved for consistent preprocessing during deployment.  

---

## Application Workflow

- Data exploration and preprocessing  
- Model training and evaluation  
- Saving trained model and scaler  
- Backend API development using FastAPI  
- Frontend user interface development using Streamlit  
- Cloud deployment using Render  

---

## Future Improvements

- Implement advanced ensemble methods (XGBoost, LightGBM).  
- Increase dataset size for improved accuracy.  
- Add real-time patient data integration.  
- Add model explainability (feature importance visualization).  

---

## Conclusion

This project demonstrates how machine learning can be applied in the healthcare domain to support early risk detection of heart disease. The system provides a complete end-to-end workflow from model development to real-time prediction through a web application.

---

## Live Application

Frontend:  
https://heart-disease-prediction-frontend-0zze.onrender.com/

Backend API Documentation:  
https://heart-disease-prediction-backend-ruxc.onrender.com/docs

EOF
