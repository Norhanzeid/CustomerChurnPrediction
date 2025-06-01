
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

- Outlier Detection & Treatment

- Applied IQR (Interquartile Range) method and Boxplots to detect and treat outliers.

## Exploratory Data Analysis (EDA) :

- Analyzed distributions and relationships of features.

- Explored how each feature impacts churn behavior.

- Using Plotly , Seaborn , Matplotlib , Pandas 

## Feature Engineering:

Created new features and encoded categorical variables to enhance model performance.


## 🔗 Clustering Analysis (Customer Segmentation) :

![1_Dvx1j18vyKyvLlIpxzVSmQ](https://github.com/user-attachments/assets/5ca5aab5-e7e0-4ac6-8edc-34a28ff4218c)


Applied K-Means Clustering to segment customers based on Tenure and Monthlycharges :

| Cluster     | Description                             |
| ----------- | --------------------------------------- |
| `Cluster 0` | High Value – High Risk (May churn)      |
| `Cluster 1` | Low Value – High Risk                   |
| `Cluster 2` | High Value – Low Risk (Loyal Customers) |


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


