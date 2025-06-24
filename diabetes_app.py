import streamlit as st
import numpy as np
import joblib
import time
from datetime import datetime

# --- Load model ---
model = joblib.load("diabetes_model.pkl")

# --- Page config ---
st.set_page_config(page_title="Diabetes Prediction | Samar Abbas", layout="centered", page_icon="🩺")

# --- Custom CSS including sidebar ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

        body {
            background-color: #f5f7fa;
        }
        .title-text {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 10px;
            font-family: 'Orbitron', sans-serif;
        }
        div.stButton > button:first-child {
            background-color: #0099ff;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-size: 16px;
        }
        div.stButton > button:first-child:hover {
            background-color: #005f99;
            transition: 0.3s ease;
        }
        .result {
            animation: fadeIn 1s ease-in-out;
        }
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        section[data-testid="stSidebar"] {
            background: rgba(20, 22, 31, 0.85);
            border: 2px solid #00ffe7;
            border-radius: 15px;
            box-shadow: 0 0 20px #00ffe7;
            padding: 20px;
            font-family: 'Orbitron', sans-serif;
        }
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            background: linear-gradient(90deg, #00ffe7, #6a5acd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Info ---
st.sidebar.markdown("<h2 style='text-align:center;'>⚙️ About App</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
**Diabetes Prediction Model**  
Enter details to predict whether 
you have the diabetes or not using ML.  

👨‍💻 Samar Abbas  
🎓 BSCS | Univ. of Narowal
""")
st.sidebar.info("Contact: **samarabbas0425@gmail.com**")

# --- Title ---
st.markdown('<div class="title-text">🩺 Diabetes Prediction App</div>', unsafe_allow_html=True)
st.markdown("""
    <h4 style='text-align: center;'>A Machine Learning Project by: <strong>Samar Abbas</strong></h4>
""", unsafe_allow_html=True)

# --- Sample Inputs ---
non_diabetic = {"pregnancies": 1, "glucose": 95, "blood_pressure": 75, "insulin": 100, "bmi": 22.5, "dpf": 0.3, "age": 28}
diabetic = {"pregnancies": 5, "glucose": 165, "blood_pressure": 88, "insulin": 200, "bmi": 32.5, "dpf": 0.85, "age": 48}

if "sample_data" not in st.session_state:
    st.session_state.sample_data = non_diabetic

st.markdown("<h4 style='text-align: center;'>🔁 Load Sample Test Cases</h4>", unsafe_allow_html=True)
colA, colB = st.columns(2)
with colA:
    if st.button("🟢 Use Non-Diabetic Sample"):
        st.session_state.sample_data = non_diabetic
with colB:
    if st.button("🔴 Use Diabetic Sample"):
        st.session_state.sample_data = diabetic

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, st.session_state.sample_data["pregnancies"])
    glucose = st.number_input("Glucose", 0, 200, st.session_state.sample_data["glucose"])
    blood_pressure = st.number_input("Blood Pressure", 0, 140, st.session_state.sample_data["blood_pressure"])
with col2:
    insulin = st.number_input("Insulin", 0, 900, st.session_state.sample_data["insulin"])
    bmi = st.number_input("BMI", 0.0, 70.0, st.session_state.sample_data["bmi"])
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, st.session_state.sample_data["dpf"])
    age = st.number_input("Age", 10, 100, st.session_state.sample_data["age"])

# --- Prediction ---
if st.button("🔍 Predict"):
    with st.spinner("Predicting..."):
        input_data = np.array([[pregnancies, glucose, blood_pressure, insulin, bmi, dpf, age]])
        proba = model.predict_proba(input_data)[0][1]
        prediction = 1 if proba >= 0.52 else 0

    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ The model predicts that the patient **has diabetes**.")
        st.markdown("**Please consult a healthcare professional.**")
    else:
        st.success("✅ The model predicts that the patient **does not have diabetes**.")
        st.markdown("**Maintain a healthy lifestyle to reduce risk.**")
    st.markdown(f"📊 **Prediction Confidence:** `{proba * 100:.2f}%`")

# --- Footer ---
st.markdown("---")
st.caption("🌟 Created with ❤️ by Samar Abbas | Powered by Scikit-learn & Streamlit")
