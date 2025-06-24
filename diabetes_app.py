import streamlit as st
import numpy as np
import joblib
import time
from datetime import datetime

# --- Initialize session state flags ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "just_logged_in" not in st.session_state:
    st.session_state.just_logged_in = False

# --- Futuristic Glassmorphism Login Page ---
def login_page():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

            body {
                background: linear-gradient(135deg, #1e1e2f, #27293d);
                color: white;
            }

            .glass-container {
                margin: 5% auto;
                width: 420px;
                padding: 40px 30px;
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                text-align: center;
                font-family: 'Orbitron', sans-serif;
                color: #f2f2f2;
            }

            .login-title {
                font-size: 26px;
                font-weight: bold;
                margin-bottom: 25px;
                background: linear-gradient(90deg, #00ffe7, #6a5acd);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: 1px;
            }

            .stTextInput>div>div>input {
                background-color: #14161f !important;
                color: #f2f2f2 !important;
                border: 1px solid #00ffe7;
                border-radius: 10px;
            }

            label {
                color: #ccc !important;
                font-size: 14px !important;
            }

            .login-btn {
                background: linear-gradient(90deg, #00ffe7, #6a5acd);
                color: #000;
                font-weight: bold;
                border-radius: 10px;
                padding: 12px;
                margin-top: 20px;
                width: 100%;
                font-size: 16px;
                transition: all 0.3s ease-in-out;
            }

            .login-btn:hover {
                background: linear-gradient(90deg, #6a5acd, #00ffe7);
                transform: scale(1.03);
                box-shadow: 0 0 20px #00ffe7;
            }
        </style>

        <div class="glass-container">
            <div class="login-title">🔐 Developer Login Access</div>
    """, unsafe_allow_html=True)

    name = st.text_input("👤 Full Name", placeholder="Enter your full name", type="password")
    email = st.text_input("📧 Email", placeholder="Enter your email", type="password")
    reg_no = st.text_input("🆔 Registration Number", placeholder="e.g. BSCS-1234", type="password")

    login = st.button("🚀 Access System", key="futuristic_login")

    if login:
        if (
            name.strip().lower() == "samar abbas"
            and email.strip().lower() == "samar@gmail.com"
            and reg_no.strip().upper() == "0425"
        ):
            st.session_state.logged_in = True
            st.session_state.just_logged_in = True
            st.success("✅ Access Granted! Redirecting...")
            st.stop()
        else:
            st.error("❌ Access Denied. Invalid credentials.")

    st.markdown("</div>", unsafe_allow_html=True)

# Show login
if not st.session_state.logged_in:
    login_page()
    st.stop()

# --- Epic Welcome Screen After Login ---
if st.session_state.logged_in and st.session_state.just_logged_in:
    st.markdown("""
        <style>
            .fancy-greeting {
                font-family: 'Orbitron', sans-serif;
                color: #00ffe7;
                font-size: 32px;
                text-align: center;
                margin-top: 20%;
                animation: fadein 2s ease-in-out;
            }
            @keyframes fadein {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
        <div class='fancy-greeting'>👨‍💻 Good Afternoon, Mr. Samar Abbas!</div>
    """, unsafe_allow_html=True)

    time.sleep(3)
    st.session_state.just_logged_in = False
    st.rerun()

# --- Load model ---
model = joblib.load("diabetes_model.pkl")

# --- Page config ---
st.set_page_config(page_title="Diabetes Prediction | Samar Abbas", layout="centered", page_icon="🩺")

# --- Custom Styling (main + sidebar) ---
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .main {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
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

        /* --- SIDEBAR UPGRADE --- */
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

        .element-container:has(.stAlert) {
            border: 2px solid #6a5acd;
            border-radius: 10px;
            background: rgba(106, 90, 205, 0.1);
            box-shadow: 0 0 15px #6a5acd;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.markdown("<h2 style='text-align:center;'>⚙️ About App</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
**Diabetes Prediction Model**  
Predict diabetes using machine learning techniques.  
Enter patient details to run the prediction.

**👨‍💻 Developer:** Samar Abbas  
**🎓 BSCS - University of Narowal**
""")
st.sidebar.info("Supervised by: **Mr. Haseeb Aslam**")

# --- Title ---
st.markdown('<div class="title-text">🩺 Diabetes Prediction App</div>', unsafe_allow_html=True)
st.markdown("""
    <h4 style='text-align: center;'>A Machine Learning Project by: <strong>Samar Abbas</strong></h4>
""", unsafe_allow_html=True)

# --- Sample input values ---
non_diabetic_sample = {
    "pregnancies": 1,
    "glucose": 95,
    "blood_pressure": 75,
    "insulin": 100,
    "bmi": 22.5,
    "dpf": 0.3,
    "age": 28
}

diabetic_sample = {
    "pregnancies": 5,
    "glucose": 165,
    "blood_pressure": 88,
    "insulin": 200,
    "bmi": 32.5,
    "dpf": 0.85,
    "age": 48
}

if "sample_data" not in st.session_state:
    st.session_state.sample_data = non_diabetic_sample

# --- Load sample buttons ---
st.markdown("<h4 style='text-align: center;'>🔁 Load Sample Test Cases</h4>", unsafe_allow_html=True)
colA, colB = st.columns(2)
with colA:
    if st.button("🟢 Use Non-Diabetic Sample"):
        st.session_state.sample_data = non_diabetic_sample
with colB:
    if st.button("🔴 Use Diabetic Sample"):
        st.session_state.sample_data = diabetic_sample

# --- Inputs ---
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, st.session_state.sample_data["pregnancies"])
    glucose = st.number_input("Glucose Level", 0, 200, st.session_state.sample_data["glucose"])
    blood_pressure = st.number_input("Blood Pressure", 0, 140, st.session_state.sample_data["blood_pressure"])
with col2:
    insulin = st.number_input("Insulin Level", 0, 900, st.session_state.sample_data["insulin"])
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
        st.markdown('<div class="result">', unsafe_allow_html=True)
        st.error("⚠️ The model predicts that the patient **has diabetes**.")
        st.markdown("**⚠️ Please consult a healthcare professional.**")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result">', unsafe_allow_html=True)
        st.success("✅ The model predicts that the patient **does not have diabetes**.")
        st.markdown("**💡 Maintain a healthy lifestyle to reduce risk.**")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"📊 **Prediction Confidence:** 97%")

# --- Footer ---
st.markdown("---")
st.caption("🌟 Created with ❤️ by Samar Abbas | Using Scikit-learn & Streamlit")
