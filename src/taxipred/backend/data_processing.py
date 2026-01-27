import pandas as pd
from taxipred.utils.constants import TAXI_CSV_PATH
from pydantic import BaseModel, Field


class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(TAXI_CSV_PATH)

    def to_json(self):
        return self.df.to_json(orient="records")
    

class TripInput(BaseModel):
    Time_of_Day: str
    Day_of_Week: str
    Traffic_Conditions: str
    Trip_Distance_km: float = Field(gt=0)
