import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


print(" Loading dataset...")
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn (1).csv')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.replace(['No phone service', 'No internet service'], 'No', inplace=True)


drop_cols = ['customerID']
target_col = 'Churn'
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
ordinal_cols = [
    'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
    'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling'
]
onehot_cols = ['InternetService', 'PaymentMethod']


print("Splitting data...")
X = df.drop(drop_cols + [target_col], axis=1)
y = df[target_col].map({'Yes': 1, 'No': 0})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


print("Building pipeline...")
preprocessor = ColumnTransformer(
    transformers=[
        ('ordinal', OrdinalEncoder(dtype=int), ordinal_cols),
        ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'), onehot_cols),
        ('scale', MinMaxScaler(), num_cols)
    ]
)

pipeline = Pipeline(steps=[
    ('preprocessing', preprocessor),
    ('classifier', LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42))
])


print("Training model...")
pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)
print("\n Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))


print(" Saving model as 'model.pkl'...")
with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("Model saved successfully as 'model.pkl'")



