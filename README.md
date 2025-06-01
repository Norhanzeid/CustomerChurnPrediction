# 📊 Customer Churn Prediction

This project predicts customer churn for a telecom company using a Logistic Regression model. The prediction is based on multiple customer features including:

Demographics: Gender, SeniorCitizen, Partner, Dependents

Customer Lifetime: Tenure

Services Subscribed: PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies

Billing Info: Contract type, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges

The model helps identify which customers are more likely to churn based on these attributes.

---

## 🔧 Tech Stack

- **Backend**: FastAPI  
- **Deployment**: Docker + Azure App Service  
- **Modeling**: Scikit-learn  
- **Dashboard**: Power BI  
- **Languages**: Python  

---

## 📁 Project Structure

```plaintext
CustomerChurnPrediction/
├── src/
│   ├── routes/             → FastAPI endpoints (FastAPI.py)
│   ├── models/             → Trained model (model.pkl)
│   ├── helpers/            → ML logic (create_model.py)
│   ├── data/               → Dataset (WA_*.csv)
│   ├── dashboard/          → Power BI dashboard (.pbit)
│   └── requirements.txt    → Python dependencies
│
├── Docker/
│   ├── Dockerfile          → Docker configuration
│   └── .dockerignore
│
└── README.md               → Project documentation


