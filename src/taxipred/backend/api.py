from taxipred.backend.data_processing import clean_text

def predict(input_text: str) -> dict:
    x = clean_text(input_text)
    return {"input": x, "prediction": 42}