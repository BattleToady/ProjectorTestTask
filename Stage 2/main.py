from fastapi import FastAPI
from pydantic import BaseModel, constr, conlist
from typing import List
import joblib
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

pipeline = joblib.load('pipeline.gz')

app = FastAPI()

class UserRequestIn(BaseModel):
    text: List[str]

class PredictOut(BaseModel):
    scores: List[float]

@app.post("/predict", response_model=PredictOut)
def read_classification(user_request_in: UserRequestIn):
    return JSONResponse(content={'scores' : list(pipeline.predict(user_request_in.text))})