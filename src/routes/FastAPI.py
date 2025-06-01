from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import pandas as pd
import pickle
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class YesNo(str, Enum):
    Yes = "Yes"
    No = "No"

class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"

class InternetServiceEnum(str, Enum):
    DSL = "DSL"
    Fiber_optic = "Fiber optic"
    No = "No"

class ContractEnum(str, Enum):
    Month_to_month = "Month-to-month"
    One_year = "One year"
    Two_year = "Two year"

class PaymentMethodEnum(str, Enum):
    Electronic_check = "Electronic check"
    Mailed_check = "Mailed check"
    Bank_transfer = "Bank transfer (automatic)"
    Credit_card = "Credit card (automatic)"

class CustomerData(BaseModel):
    gender: GenderEnum
    SeniorCitizen: int
    Partner: YesNo
    Dependents: YesNo
    tenure: int
    PhoneService: YesNo
    MultipleLines: YesNo
    InternetService: InternetServiceEnum
    OnlineSecurity: YesNo
    OnlineBackup: YesNo
    DeviceProtection: YesNo
    TechSupport: YesNo
    StreamingTV: YesNo
    StreamingMovies: YesNo
    Contract: ContractEnum
    PaperlessBilling: YesNo
    PaymentMethod: PaymentMethodEnum
    MonthlyCharges: float
    TotalCharges: float

def preprocess(df):
    df.replace(['No phone service', 'No internet service'], 'No', inplace=True)
    return df

@app.post("/predict")
async def predict(data: CustomerData):
    input_df = pd.DataFrame([data.model_dump()])
    input_df = preprocess(input_df)
    prediction = model.predict(input_df)[0]
    result = "Customer is likely to churn" if prediction == 1 else "Customer is likely to stay"
    return {"prediction": int(prediction), "result": result}
