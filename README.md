
![1705526647346 (1)](https://github.com/user-attachments/assets/1eb8cf32-7f33-478c-8130-d380f3c3149c)


# 📊 Customer Churn Prediction  


This project predicts customer churn for a telecom company . The prediction is based on multiple customer features including:

- Demographics : Gender, SeniorCitizen, Partner, Dependents

- Customer Lifetime : Tenure

- Services Subscribed : PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies

- Billing Info : Contract type, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges


---
## 🔍 Project Overview :

This project predicts customer churn for a telecom company using various machine learning models, advanced preprocessing techniques, and customer segmentation via clustering. The project includes:
    
⚙️ Steps Followed :

- Identified and handled missing values using appropriate imputation techniques.

- Applied IQR (Interquartile Range) method and Boxplots to detect and treat outliers.

## Exploratory Data Analysis (EDA) :

- Analyzed distributions and relationships of features.

- Explored how each feature impacts churn behavior.

- Using Plotly , Seaborn , Matplotlib , Pandas 

## Feature Engineering:

Created new features and encoded categorical variables to enhance model performance.


## 🔗 Clustering Analysis (Customer Segmentation) :

![1_Dvx1j18vyKyvLlIpxzVSmQ](https://github.com/user-attachments/assets/1beb5d96-8ee8-4782-a00d-324a6b4c7d8f)


Applied K-Means Clustering to segment customers based on Tenure and Monthlycharges :

| Cluster     | Description                             |
| ----------- | --------------------------------------- |
| `Cluster 0` | High Value – High Risk (May churn)      |
| `Cluster 1` | Low Value – High Risk                   |
| `Cluster 2` | High Value – Low Risk (Loyal Customers) |


![Screenshot (1329)](https://github.com/user-attachments/assets/39e86651-5d67-47f1-b0bb-4974d4320fa9)


## Model Building:

# Trained and evaluated multiple classification models:

- Logistic Regression

- Support Vector Classifier (SVC)

- Random Forest Classifier


## Handling Class Imbalance

Applied resampling techniques:

- SMOTE

- ADASYN

- SMOTEEN (SMOTE + Edited Nearest Neighbors)


## 🚀 Deployment Architecture:

The trained model is deployed using a modern MLOps stack as follows:

✅ FastAPI: To serve the prediction API (receives input from users and returns churn prediction).

🐳 Docker: Containerizes the application to ensure consistent behavior across environments.

☁️ Azure App Service: Hosts the Docker container using Azure Container Registry (ACR) for seamless deployment.

🚀 Live App : https://churnwebapp-etd4efbvbwg2c9bf.uaenorth-01.azurewebsites.net/

![Screenshot (1327)](https://github.com/user-attachments/assets/79b839e7-a231-4aea-a16c-7cd657354f7c)


✳️ How it works:

- User submits form data via frontend.

- Frontend sends POST request to FastAPI endpoint (/predict).

- FastAPI loads model.pkl and performs prediction.

- Docker ensures this whole service is containerized.

- Azure App Service pulls the Docker image and serves it as a web app.


## 🔧 Tech Stack

- **Backend**: FastAPI  
- **Deployment**: Docker + Azure App Service  
- **Modeling**: Scikit-learn  
- **Dashboard**: Power BI  
- **Languages**: Python  

---


## Power BI Dashboard  :

![Screenshot (1361)](https://github.com/user-attachments/assets/38d500d0-4f87-44bb-bf72-751017a9a717)

![Screenshot (1362)](https://github.com/user-attachments/assets/ef476d96-5077-4695-b31e-6d7421c7ec4b)



## 📁 Project Structure

```plaintext
CustomerChurnPrediction/
├── src/
│   ├── routes/             → FastAPI endpoints (FastAPI.py)
│   ├── models/             → Trained model (model.pkl)
│   ├── helpers/            → ML logic (Model.py)
│   ├── data/               → Dataset (WA_*.csv)
│   ├── dashboard/          → Power BI dashboard (.pbit)
│   └── requirements.txt    → Python dependencies
│
├── Docker/
│   ├── Dockerfile          → Docker configuration
│   └── .dockerignore
│
└── README.md               → Project documentation

