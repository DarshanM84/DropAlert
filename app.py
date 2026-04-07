import streamlit as st
import pickle
import numpy as np

# Page config (important for single screen layout)
st.set_page_config(page_title="DropAlert", layout="wide")

# Load model
model = pickle.load(open('Model/dropout_model.pkl', 'rb'))

# Title
st.markdown("""
<h1 style='text-align: center;'>🎓 DropAlert - DropOut Risk Predictor</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout using columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Academic Details")
    cgpa = st.slider("CGPA", 0.0, 10.0)
    attendance = st.slider("Attendance (%)", 0, 100)

with col2:
    st.markdown("### 🧪 Engagement Details")
    assignments = st.slider("Assignments Submitted (0–30)", 0, 30)
    lab_hours = st.slider("Lab Hours per Week (0–15)", 0, 15)
    counsellor = st.slider("Counsellor Visits (0–5)", 0, 5)

st.markdown("---")

# Center button
_, col_btn, _ = st.columns([1, 1, 1])
with col_btn:
    predict = st.button("🚀 Predict Risk")

# Prediction
if predict:
    data = np.array([[float(cgpa), float(attendance), float(assignments), float(lab_hours), float(counsellor)]])
    risk_score = model.predict_proba(data)[0][1]

    # Risk Level Logic
    if cgpa >= 8 and attendance >= 80:
        level = "🟢 Safe"
    elif risk_score > 0.65:
        level = "🔴 Critical"
    elif risk_score > 0.3:
        level = "🟠 At Risk"
    else:
        level = "🟢 Safe"

    # Reason Logic
    if cgpa < 6:
        reason = "Low CGPA"
    elif attendance < 60:
        reason = "Low Attendance"
    elif assignments < 10:
        reason = "Low Assignment Submission"
    else:
        reason = "Good performance"

    st.markdown("## 🎯 Prediction Result")

    # Colored output
    if "Critical" in level:
        st.error(f"Risk Level: {level}")
    elif "At Risk" in level:
        st.warning(f"Risk Level: {level}")
    else:
        st.success(f"Risk Level: {level}")

    # Risk Score as progress bar
    st.progress(float(risk_score))
    st.write(f"📊 Risk Score: {risk_score:.2f}")

    # Reason
    st.info(f"📌 Reason: {reason}")

    # Input summary
    st.caption(f"Input → CGPA: {cgpa}, Attendance: {attendance}")