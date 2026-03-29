# 🔥 Forest Fire Weather Index Prediction System

## 📌 Project Overview
This project is an end-to-end Machine Learning web application that predicts the Fire Weather Index (FWI) using weather and environmental conditions.

It integrates:
- Data preprocessing
- Machine Learning model (Ridge Regression)
- Model persistence using Pickle
- Flask web application
- Deployment on Render
- Docker support

---

## 🚀 Live Demo
Deployed Application:
https://testforestfires-3-v3ee.onrender.com

---

## 🧠 Problem Statement
Forest fires are influenced by environmental and weather conditions.  
This project predicts the Fire Weather Index (FWI) to estimate fire danger levels.

Helps in:
- Fire risk prediction
- Environmental monitoring
- Early warning systems

---

## ⚙️ Tech Stack
- Python  
- Flask  
- Scikit-learn  
- NumPy  
- Pandas  
- Pickle  
- HTML/CSS  
- Gunicorn  
- Render  
- Docker  

---

## 📂 Project Structure
testforestfires/
│
├── .ebextensions/
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
├── notebook/
├── templates/
│   ├── home.html
│   └── index.html
├── application.py
├── requirements.txt
└── README.md

---

## 📥 Input Features
- Temperature  
- Relative Humidity (RH)  
- Wind Speed (Ws)  
- Rain  
- FFMC  
- DMC  
- ISI  
- Classes  
- Region  

---

## 📤 Output
Predicted Fire Weather Index (FWI)

Example:
Predicted FWI = 12.37

Higher FWI means higher fire risk.

---

## 🔬 Machine Learning Workflow
1. Data preprocessing  
2. Feature scaling using StandardScaler  
3. Model training (Ridge Regression)  
4. Model saving (.pkl files)  
5. Flask integration  
6. Prediction via UI  

---

## 🌐 Web Application Flow
1. User enters input values  
2. Data is sent to Flask backend  
3. Data is scaled  
4. Model predicts FWI  
5. Result is displayed  

---

## ▶️ Run Locally

1. Clone repository
git clone https://github.com/divyasreevemula918/testforestfires.git
cd testforestfires

2. Create virtual environment
python -m venv venv

3. Activate environment
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run application
python application.py

6. Open browser
http://127.0.0.1:5000/

---

## ☁️ Deployment (Render)

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn application:app

---

## 🐳 Docker Setup

Build image:
docker build -t forest-fire-app .

Run container:
docker run -p 5000:5000 forest-fire-app

Access:
http://localhost:5000/

---

## 💡 Use Case
Example:
High temperature  
Low rainfall  
Strong wind  

Model predicts fire risk using FWI.

---

## 📈 Future Improvements
- Improve UI design  
- Add multiple ML models  
- Add real-time data  
- Add charts and visualization  
- CI/CD pipeline  

---

## 🙌 Author
Divya Sree Vemula

GitHub: https://github.com/divyasreevemula918  
Project Repo: https://github.com/divyasreevemula918/testforestfires  
Live App: https://testforestfires-3-v3ee.onrender.com

---
