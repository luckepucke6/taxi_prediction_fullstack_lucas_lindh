import pandas as pd
from taxipred.utils.constants import taxi_csv_path

class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(taxi_csv_path)

    def to_json(self):
        return self.df.to_json(orient="records")