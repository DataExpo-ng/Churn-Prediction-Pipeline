# fastapi -- framework for building APIs
# uvicorn -- Server to run the API
# pydantic -- validates input data
# joblib -- load our saved model



# step 1 - creating a simple api
from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np

# step 2 - create API instance
app = FastAPI(title="Churn Prediction API")

# step 3 create a simple endpoint --- the address of the API
# - www.facebook.com  - an endpoint/address
# - google.com/careers - an endpoint
# google takes you to the career page

# - www.predictions_with_mo/logistic_regression ---
# input name
# input nphone number
# other details
# Model (Logistic reg, Random F or Xgboost) -- process the input data
# Get predictions

# get request ---- user is seeking for information 
# post request ---- user is seeking for information - giving a clue or some input data



# define what customers data we are expecting
class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    Contract: str
    InternetService: str
    PaymentMethod: str


    # Example of input data
    class config:
        schema_extra = {
            "example": {
                "tenure": 12,
                "MonthlyCharges": 29.85,
                "TotalCharges":  298.5,
                "Contract": "Month-to-month",
                "InternetService": "DSL",
                "PaymentMethod": "Electronic check"
            }
        }


# Load our model - step 1
# download the model from s3 bucket -- which we've already done in dowload_model.py

# load the model into the app
print("loading model....")
model = joblib.load('logistic_regression_model.joblib')
print("model loaded....")

# step 3 - update the default endpoint
@app.get("/")  #get request #facebook.com - sign up and sign up
def home():
    return {"message": "Welcome to Churn prediction API",
            "model_loaded": True,
            "version": "1.0.0" 
            }


# step 4 - update the /health endpoint
# create health endpoint
@app.get("/health")
def health():
    return {"status": "healthy",
            "model": "loaded"
            
            }


# step 5 - create prediction endpoint
@app.post("/predict")
def predict_churn(customer: CustomerData):

    # step 5a -  preprocess the input data
    # convert pydantic model to dictionary
    customer_data = customer.dict()
    print("customer data: ", customer_data)

    # convert dictionary to dataframe
    import pandas as pd 
    customer_df = pd.DataFrame([customer_data])
    print("customer df: ", customer_df)

    # define the feature columns and convert to what model expects accordingly to the pydantic model

    feature_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']


    # step 5b - make predictions
    prediction = model.predict(customer_df)
    prediction_proba = model.predict_proba(customer_df)
    print("prediction: ", prediction)
    print("prediction proba: ", prediction_proba)

    # step 5c - return the predictions
    return {
        "churn_prediction": int(prediction[0]),
        "churn_probability": {
            "no_churn": float(prediction_proba[0][0]),
            "churn": float(prediction_proba[0][1])
        }
    }

