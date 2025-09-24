# Student Performance Prediction - End-to-End Machine Learning Project

## Overview

This project predicts students' math scores based on demographic and academic features using various regression models. It demonstrates a complete ML workflow including data ingestion, preprocessing, model training, evaluation, and deployment with a Flask web interface.

## Features

- Data ingestion and preprocessing pipeline
- Multiple regression models (Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, CatBoost, AdaBoost)
- Hyperparameter tuning with GridSearchCV
- Model evaluation and selection
- Model persistence (pickle)
- Flask web app for predictions
- Jupyter notebooks for EDA and model training
- Logging and exception handling

## Project Structure

```
mlproject-main/
│
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── setup.py                # Project setup for pip installation
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
│
├── artifacts/              # Saved models, preprocessors, and datasets
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── data.csv
│
├── catboost_info/          # CatBoost training logs and metrics
│   ├── catboost_training.json
│   ├── learn_error.tsv
│   ├── time_left.tsv
│   └── learn/
│       └── events.out.tfevents
│
├── notebook/               # Jupyter notebooks for EDA and training
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── catboost_info/
│       ├── catboost_training.json
│       ├── learn_error.tsv
│       ├── time_left.tsv
│       └── learn/
│           └── events.out.tfevents
│   └── data/
│       └── stud.csv
│
├── src/                    # Source code
│   ├── __init__.py
│   ├── exception.py        # Custom exception class
│   ├── logger.py           # Logging configuration
│   ├── utils.py            # Utility functions (model evaluation, save/load objects)
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py      # Data ingestion logic
│   │   ├── data_transformation.py # Data preprocessing logic
│   │   └── model_trainer.py       # Model training and selection
│   └── pipeline/
│       ├── __init__.py
│       ├── predict_pipeline.py    # Prediction pipeline for web app
│       └── train_pipeline.py      # Training pipeline script
│
├── templates/              # HTML templates for Flask app
│   ├── home.html
│   └── index.html
│
├── .ebextensions/          # Elastic Beanstalk config (for deployment)
│   └── python.config
├── .github/
│   └── workflows/
│       └── main_studentssperformance3.yml
```

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd mlproject-main
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```sh
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage

- **Web Interface:**  
  Go to `/predictdata` and enter student details to predict math score.

- **Jupyter Notebooks:**  
  Use notebooks in `notebook/` for exploratory data analysis and model training.

- **Training Pipeline:**  
  Run the training pipeline in [`src/pipeline/train_pipeline.py`](src/pipeline/train_pipeline.py) to retrain models.

## Key Files

- [`src/components/data_ingestion.py`](src/components/data_ingestion.py): Loads and splits raw data.
- [`src/components/data_transformation.py`](src/components/data_transformation.py): Preprocessing and feature engineering.
- [`src/components/model_trainer.py`](src/components/model_trainer.py): Model training, hyperparameter tuning, and selection.
- [`src/pipeline/predict_pipeline.py`](src/pipeline/predict_pipeline.py): Loads model and preprocessor for predictions.
- [`src/utils.py`](src/utils.py): Utility functions for saving/loading objects and evaluating models.
- [`app.py`](app.py): Flask web server.

## Model Training & Evaluation

- Models are trained using GridSearchCV for hyperparameter tuning.
- Evaluation metrics include R² score and RMSE.
- Best model is saved to `artifacts/model.pkl`.

## Deployment

- Ready for deployment on platforms like Azure Web Apps (see `.github/workflows/main_studentssperformance3.yml` and `.ebextensions/python.config`).

## Logging & Exception Handling

- Logging is configured in [`src/logger.py`](src/logger.py).
- Custom exceptions are handled via [`src/exception.py`](src/exception.py).

## Contributing

Feel free to fork the repo and submit pull requests.

## License

This project is for educational purposes.

## Author

Manav Gupta
