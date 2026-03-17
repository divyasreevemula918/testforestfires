# 🌲 Forest Fire Weather Index Prediction System

## 📌 Project Overview
This project is an end-to-end Machine Learning web application that predicts the **Fire Weather Index (FWI)** using weather and fire-related input features.

The workflow includes:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Serialization
- Flask-based Web Application for Prediction

---

## 🚀 Features
- Predicts **FWI (Fire Weather Index)** from user input
- Uses a saved **Ridge Regression** model for prediction
- Uses a saved **StandardScaler** for preprocessing
- Web interface built using **Flask**
- Separate notebook workflow for EDA and training
- Loads model artifacts from the `models/` folder

---

## 🧠 Problem Statement
Forest fire risk can be estimated from environmental and weather conditions.

This project uses machine learning to predict the **Fire Weather Index (FWI)** based on important features such as temperature, humidity, wind speed, rainfall, and fire-related indices.

---

## 📥 Input Features
The model takes the following 9 input features:

- Temperature
- RH (Relative Humidity)
- Ws (Wind Speed)
- Rain
- FFMC
- DMC
- ISI
- Classes
- Region

### Example Input
- Temperature = 30
- RH = 45
- Ws = 15
- Rain = 0
- FFMC = 85
- DMC = 26
- ISI = 5
- Classes = 1
- Region = 2

---

## 📤 Output
The model returns a **single predicted FWI value**.

### Example Output
- Predicted FWI = `12.37`

### What the output means
- Lower FWI → lower fire danger
- Higher FWI → higher fire danger

---

## 🏗️ Project Structure

```text
testforestfires/
│
├── .ebextensions/                     # Deployment-related config
├── models/
│   ├── ridge.pkl                      # Trained Ridge Regression model
│   └── scaler.pkl                     # Saved StandardScaler
├── notebook/                          # EDA and model training notebooks
├── templates/
│   ├── index.html                     # Homepage
│   └── home.html                      # Prediction result page
├── application.py                     # Flask application
├── requirements.txt                   # Project dependencies
└── README.md
