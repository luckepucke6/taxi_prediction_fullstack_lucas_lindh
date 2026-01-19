from pathlib import Path

PROJECT_NAME = "taxipred"
BASE_DIR = Path(__file__).resolve().parents[3]
TAXI_CSV_PATH = BASE_DIR / "src" / "taxipred" / "data" / "clean_taxi_data.csv"

label = "Trip_Price"


features = [
  "Time_of_Day",
  "Day_of_Week",
  "Passenger_Count",
  "Traffic_Conditions",
  "Trip_Distance_km"
]
