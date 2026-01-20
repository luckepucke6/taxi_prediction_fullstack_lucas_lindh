from fastapi import FastAPI
from taxipred.backend.data_processing import TaxiData, TripInput
from taxipred.utils.constants import MODEL_PATH, PREPROCESSOR_PATH
import joblib
import pandas as pd

app = FastAPI()
taxi_data = TaxiData()
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)
USD_TO_SEK = 10.5

@app.get("/taxi")
async def read_taxi_data():
    return taxi_data.to_json()

@app.post("/predict")
async def predict(trip: TripInput):
    # Pydantic -> dict
    data = trip.model_dump()

    # dict -> dataframe
    df = pd.DataFrame([data])

    # preprocessing
    X = preprocessor.transform(df)

    # prediction 
    prediction = model.predict(X)

    price_usd = float(prediction[0])
    price_sek = price_usd * USD_TO_SEK

    # return response
    return {
        "predicted_price_usd": price_usd,
        "predicted_price_sek": price_sek,
        "exchange_rate": USD_TO_SEK
    }

# 1. Ladda in preprocessor + model (joblib)
# 2. Definera /predict endpoint
# 3. Input: TripInput (pydantic)
# 4. Konvertera input till DataFrame
# 5. preprocessor.transform
# 6. model.predict
# 7. Returnera priset