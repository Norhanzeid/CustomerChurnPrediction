# 📊 Customer Churn Prediction

This project predicts customer churn for a telecom company using a trained machine learning model. The project is deployed using FastAPI, Docker, and hosted on Azure.

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


