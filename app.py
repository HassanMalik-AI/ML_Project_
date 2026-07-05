from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = FastAPI()

# Mount static files for CSS and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    # Pass the 'request' object in the context
    return templates.TemplateResponse("index.html", {"request": request})

import sys
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException

@app.post('/predict')
async def predict_datapoint(
    request: Request,
    gender: str = Form(...),
    ethnicity: str = Form(...),
    parental_level_of_education: str = Form(...),
    lunch: str = Form(...),
    test_preparation_course: str = Form(...),
    reading_score: float = Form(...),
    writing_score: float = Form(...)
):
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        pred_df = data.get_data_as_data_frame()
        print("Incoming Data:", pred_df)
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        predicted_score = round(results[0], 2)
        
        return JSONResponse(content={
            "math_score": predicted_score
        })
    except Exception as e:
        print(f"Error making prediction: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})