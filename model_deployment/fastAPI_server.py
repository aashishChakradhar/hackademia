from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib

app = FastAPI()

model = joblib.load('iris_logistic_regression.pkl')

class Features(BaseModel):
    features: conlist(float,min_length=4,max_length=4)


@app.post('/predict')
def predict(data:Features):
    try:
        prediction = model.predict([data.features])
        return {'prediction':int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))