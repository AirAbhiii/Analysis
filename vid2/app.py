from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Initialize the app and load the model
app = FastAPI()
model = joblib.load("LinearModel.pkl")

# Define input data model
class InputData(BaseModel):
    input1: float
    input2: float

# Define endpoint
@app.post("/predict/")
def predict(data: InputData):
    input_values = [[data.input1, data.input2]]
    prediction = model.predict(input_values)[0]
    return {"prediction": prediction}
