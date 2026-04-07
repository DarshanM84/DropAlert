# 🎓 DropAlert – Student Dropout Early Warning System

## 📌 Overview

**DropAlert** is a machine learning-based system designed to identify students at risk of dropping out.
It analyzes academic and behavioral data to generate a **risk score**, classify students into risk levels, and provide **explainable reasons**.

---

## 🚀 Features

* 📊 Predicts student dropout risk using ML model
* 🎯 Generates **risk score (0–1 probability)**
* 🚦 Classifies students into:

  * 🟢 Safe
  * 🟠 At Risk
  * 🔴 Critical
* 💡 Provides **reason for prediction** (explainability)
* 🌐 Interactive **Streamlit web app**
* 📈 EDA insights and feature analysis

---

## 🧠 Key Insights (EDA)

* Students with **low CGPA** are more likely to drop out
* **Lower attendance** increases dropout risk
* **Counsellor visits** show minimal impact

---

## 🤖 Model Details

* Algorithm: **Random Forest Classifier**
* Evaluation Metrics:

  * Accuracy: ~72%
  * Precision: ~65%
  * Recall: ~46%

> Note: Recall can be improved further using class balancing techniques.

---

## 📁 Project Structure

```
DropAlert/
│
├── data/
├── notebooks/
│   └── Drop_Alert.ipynb
│
├── Model/
│   └── dropout_model.pkl
│
├── app.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/dropalert.git
cd dropalert
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Application

```
streamlit run app.py
```

---

## 🌐 Usage

1. Enter student details:

   * CGPA
   * Attendance
   * Assignments
   * Lab hours
   * Counsellor visits

2. Click **Predict Risk**

3. View:

   * Risk Score
   * Risk Level
   * Reason for prediction

---

## 🎯 Sample Output

* Risk Score: 0.65
* Risk Level: 🟠 At Risk
* Reason: Low CGPA

---

## 💡 Future Improvements

* Improve recall using class balancing
* Add more features (failures, behavior tracking)
* Deploy on cloud (Streamlit Cloud / AWS)
* Add dashboard visualizations

---

## 🏆 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib, Seaborn

---

## 👨‍💻 Author

**Darshan M**

---

## ⭐ Acknowledgment

This project was developed as part of a data science challenge to build an early warning system for student dropout prediction.

---
