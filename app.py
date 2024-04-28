from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel
from data_preprocessing import preprocess_url_features

# Define a data model for input data validation (we are just checking a str here)
class URLData(BaseModel):
    url: str

app = FastAPI()

# Load the pre-trained model
model = joblib.load('phishing_probability_predictor_model.pkl')

@app.post("/predict/")
async def predict_phishing(data: URLData):
    # Preprocess the URL to extract features
    try:
        features = preprocess_url_features(data.url)
        features_df = pd.DataFrame([features])
        predictions = model.predict_proba(features_df)[:, 1] 
        phishing_probability = predictions[0] * 100.
        is_phishing = "phishing" if phishing_probability >= 70.0 else "not phishing"
        return {"probability": f"{phishing_probability:.3f}%", "classification": is_phishing}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

