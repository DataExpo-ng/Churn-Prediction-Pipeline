# ☁️ Cloud-Native Customer Churn Prediction Pipeline

An end-to-end **data science + MLOps project** designed for cloud engineers, data scientists, and interns at **DATEXPO**.  
This project demonstrates how to build, deploy, and monitor a production-ready **churn prediction model** using AWS services and open-source tools.

---

## 🎯 Project Overview

**Goal:** Predict customer churn for a telecom company using a fully cloud-integrated ML pipeline.  
**Dataset:** [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)  
**Cloud Platform:** AWS (S3, SageMaker, Lambda, API Gateway, CloudWatch)  
**Key Deliverable:** A live REST API that predicts customer churn and explains results using SHAP.

---

## 🧩 Architecture Overview

```text
Kaggle Dataset → AWS S3 → SageMaker (EDA + Feature Eng.) → Model Training
       ↓
   XGBoost Model + SHAP → Dockerized Flask API → AWS Lambda via API Gateway
       ↓
   Streamlit Dashboard → AWS CloudWatch Monitoring → CI/CD (GitHub Actions)
```

<p align="center">
  <img src="docs/architecture_diagram.png" width="600" alt="Architecture Diagram"/>
</p>

---

## 🪜 Project Pipeline

### 1️⃣ Data Ingestion & Storage

- Source: Kaggle Dataset
- Storage: AWS S3 (`raw/` and `processed/` folders)
- Scripts: `src/data_ingestion.py`
- Output: `data/processed/churn_processed.csv`

### 2️⃣ Data Processing & Feature Engineering

- Tools: Pandas, NumPy, Matplotlib
- Tasks: Missing value handling, encoding, feature creation (`total_services_used`)
- Output saved to: S3 → `processed/`

### 3️⃣ Model Training & Explainability

- Algorithm: XGBoost
- Platform: AWS SageMaker Training Job
- Explainability: SHAP for feature importance and individual explanations
- Output: `model/xgboost_churn.pkl` (stored in S3)

### 4️⃣ API Deployment

- Framework: FastAPI / Flask
- Containerization: Docker + AWS Lambda
- Endpoint: `/predict`
- Example:

  ```bash
  curl -X POST https://api.datexpo.org/predict -H "Content-Type: application/json" -d '{"tenure": 12, "MonthlyCharges": 70.2}'
  ```

### 5️⃣ Dashboarding

- Tool: Streamlit
- Features:

  - Input form for customer details
  - Real-time churn probability
  - SHAP feature explanation chart

- File: `streamlit_app/dashboard.py`

### 6️⃣ CI/CD & Monitoring

- **Automation:** GitHub Actions → Docker build → ECR → Lambda
- **Monitoring:** AWS CloudWatch for latency, invocations, and drift alerts

---

## 🧠 Tech Stack

| Category            | Tools                                              |
| ------------------- | -------------------------------------------------- |
| **Data & ML**       | Python, Pandas, Scikit-learn, XGBoost, SHAP        |
| **Cloud**           | AWS S3, SageMaker, Lambda, API Gateway, CloudWatch |
| **API & DevOps**    | Flask, FastAPI, Docker, GitHub Actions             |
| **Visualization**   | Streamlit, Power BI                                |
| **Version Control** | Git, GitHub                                        |

---

## 🧪 Local Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/DataExpo-ng/Churn-Prediction-Pipeline.git
   cd Churn-Prediction-Pipeline
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API Locally**

   ```bash
   cd api
   uvicorn app:app --reload
   ```

4. **Access the Dashboard**

   ```bash
   streamlit run streamlit_app/dashboard.py
   ```

---

## 🚀 Deployment (CI/CD Flow)

```text
Push to Main Branch → GitHub Actions Builds Docker → ECR Upload → Lambda Update
```

✅ Fully automated serverless deployment via GitHub Actions.
✅ Logs and metrics monitored in AWS CloudWatch.

---

## 📊 Results & Explainability

- Model Accuracy: 87%
- F1-Score: 0.84
- Key Drivers: Contract Type, Tenure, Monthly Charges
- Explainability: SHAP plots highlight top churn factors per customer.

<p align="center">
  <img src="docs/shap_summary_plot.png" width="600" alt="SHAP Plot"/>
</p>

---

## 🧑‍💻 Contributors

| Name                 | Role              | Focus Area                        |
| -------------------- | ----------------- | --------------------------------- |
| **Edwin Acheampong** | Data Scientist    | Model Training, XAI               |
| **DATEXPO Interns**  | Mentees           | EDA, Feature Engineering, Testing |
| **Mentors**          | Project Reviewers | DevOps, Architecture, Cloud Setup |

---

## 📬 Contact

📧 **[hello@datexpo.org](mailto:hello@datexpo.org)**
🌐 [datexpo.org](https://datexpo.org)
💼 [GitHub Organization](https://github.com/DataExpo-ng)

---

<p align="center">
  <i>“Learning by doing — Data by practice.”</i><br>
  © 2025 DATEXPO Cloud & Data Mentorship
</p>

---
