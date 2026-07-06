# Student Performance Prediction

## Overview
This project is an end-to-end Machine Learning web application built to predict a student's math score based on various demographic and educational features. It takes into account factors such as gender, race/ethnicity, parental level of education, lunch type, test preparation courses, reading scores, and writing scores. 

The application provides a user-friendly web interface served via **FastAPI** to input student details and instantly get the predicted math score.

## Features
- **End-to-End ML Pipeline**: Includes data ingestion, data transformation, and model training components.
- **Web Interface**: A responsive HTML frontend styled and served using FastAPI and Jinja2 Templates.
- **RESTful API Endpoint**: An endpoint (`/predict`) to submit form data and receive predictions.
- **Custom Logging & Exception Handling**: Robust tracking of application flow and errors.

## Tech Stack
- **Backend Framework**: FastAPI
- **Machine Learning**: Scikit-Learn, XGBoost, CatBoost
- **Data Manipulation**: Pandas, NumPy
- **Frontend**: HTML5, CSS (Jinja2 Templates)

## Directory Structure
The project is organized in a modular and professional manner:

```text
├── app.py                      # FastAPI application entry point and API routes
├── requirements.txt            # Python dependencies required for the project
├── setup.py                    # Script to build the project as a local Python package
├── src/                        # Main source code directory
│   ├── component/              # Core Machine Learning components
│   │   ├── data_ingestion.py   # Ingests raw data and saves it for processing
│   │   ├── data_transformation.py # Preprocesses and transforms data for the model
│   │   └── model_trainer.py    # Trains various ML models and saves the best one
│   ├── pipeline/               # Orchestration pipelines
│   │   ├── predict_pipeline.py # Loads the model/preprocessor and predicts on new data
│   │   └── train.pipeline.py   # Orchestrates the end-to-end training process
│   ├── exception.py            # Custom exception handling for better debugging
│   ├── logger.py               # Custom logging configuration
│   └── utils.py                # Helper functions (e.g., saving/loading objects)
├── artifacts/                  # Stores generated outputs (models, preprocessors, cleaned data)
├── notebook/                   # Jupyter notebooks for Exploratory Data Analysis (EDA) and Model Training experiments
├── static/                     # Static web assets (CSS, JavaScript, Images)
├── templates/                  # Jinja2 HTML templates (e.g., index.html)
└── logs/                       # Application execution and error logs
```

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI server:**
   ```bash
   uvicorn app:app --reload
   ```

2. **Access the application:**
   Open your web browser and navigate to: `http://localhost:8000`

3. **Make a Prediction:**
   Fill out the form on the home page with the required student information and submit it to see the predicted math score.