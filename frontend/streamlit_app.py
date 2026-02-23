import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction System",
    layout="wide"
)

st.title("Heart Disease Risk Assessment")
st.markdown("Clinical Decision Support Interface")
st.markdown("---")


# -----------------------------
# Sidebar Input Section
# -----------------------------
st.sidebar.header("Patient Information")

age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=52)
sex = st.sidebar.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.sidebar.selectbox("Chest Pain Type", options=[0, 1, 2, 3])
trestbps = st.sidebar.number_input("Resting Blood Pressure", value=125)
chol = st.sidebar.number_input("Cholesterol", value=212)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
restecg = st.sidebar.selectbox("Resting ECG", options=[0, 1, 2])
thalach = st.sidebar.number_input("Maximum Heart Rate Achieved", value=168)
exang = st.sidebar.selectbox("Exercise Induced Angina", options=[0, 1])
oldpeak = st.sidebar.number_input("ST Depression", value=1.0)
slope = st.sidebar.selectbox("Slope of ST Segment", options=[0, 1, 2])
ca = st.sidebar.selectbox("Number of Major Vessels", options=[0, 1, 2, 3])
thal = st.sidebar.selectbox("Thalassemia", options=[0, 1, 2, 3])


# -----------------------------
# Prediction Section
# -----------------------------
st.subheader("Prediction Result")

if st.button("Generate Prediction"):

    input_data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    with st.spinner("Processing prediction..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=input_data
            )

            if response.status_code == 200:

                result = response.json()

                prediction = result["prediction"]
                probability = result["probability"]
                risk_level = result["risk_level"]
                interpretation = result["interpretation"]

                st.markdown("---")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### Risk Classification")
                    if prediction == 1:
                        st.error(risk_level)
                    else:
                        st.success(risk_level)

                with col2:
                    st.markdown("### Predicted Probability")
                    st.metric(
                        label="Probability of Heart Disease",
                        value=f"{probability}%"
                    )

                st.markdown("---")
                st.markdown("### Clinical Interpretation")
                st.write(interpretation)

            else:
                st.error("Prediction service unavailable.")

        except Exception as e:
            st.error(f"Connection error: {e}")


st.markdown("---")
st.caption("Machine Learning Based Heart Disease Prediction System")