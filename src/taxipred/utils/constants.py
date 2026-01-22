from pathlib import Path

PROJECT_NAME = "taxipred"
BASE_DIR = Path(__file__).resolve().parents[3]
TAXI_CSV_PATH = BASE_DIR / "src" / "taxipred" / "data" / "clean_taxi_data.csv"
MODEL_PATH = BASE_DIR / "src" / "taxipred" / "backend" / "models" / "random_forest_model.joblib"
PREPROCESSOR_PATH = BASE_DIR / "src" / "taxipred" / "backend" / "models" / "preprocessor.joblib"
TAXI_PATH = Path(__file__).parents[1] / "data" / "taxi.jpg"

label = "Trip_Price"


features = [
  "Time_of_Day",
  "Day_of_Week",
  "Passenger_Count",
  "Traffic_Conditions",
  "Trip_Distance_km"
]
