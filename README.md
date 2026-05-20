# HR Attrition Prediction —- Machine Learning Web App

A Streamlit web application that runs a complete machine learning pipeline to predict
employee attrition. Upload your HR dataset and the app handles everything from
data exploration to model evaluation and live predictions.

---

## What the App Does

1. Loads and explores the HR dataset (shape, types, missing values, distributions)
2. Preprocesses the data (outlier removal, encoding, scaling, SMOTE balancing)
3. Trains four classification models: Logistic Regression, Decision Tree, Random Forest, KNN
4. Evaluates all models with accuracy, precision, recall, F1, ROC-AUC, and confusion matrices
5. Performs hyperparameter tuning with GridSearchCV and RandomizedSearchCV
6. Displays feature importance and business recommendations
7. Lets you enter employee details and predict attrition risk in real time

---

## Setup

### 1. Enter the project folder
```bash
cd hr_attrition_app
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

Opens at http://localhost:8501

---

## Dataset

Upload the HR-Employee-Attrition.csv file (IBM HR Analytics dataset).
You can download it from: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

---

## How to Use

1. Upload the CSV file using the sidebar
2. Click each step button in order, or click "Run Full Pipeline" to run everything at once
3. Scroll down to see results for each step
4. Use the Live Employee Attrition Predictor at the bottom to test individual employees

---

## Project Structure

```
hr_attrition_app/
    app.py              Main Streamlit application
    requirements.txt    Python dependencies
    README.md           This file
```
