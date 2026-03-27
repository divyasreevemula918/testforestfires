from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize app
app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('models/ridge.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Home route → shows UI page
@app.route('/')
def home():
    return render_template('index.html')   # 👉 change to 'home.html' if needed

# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Get values from form
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Prepare input
            data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
            scaled_data = scaler.transform(data)

            # Prediction
            result = model.predict(scaled_data)[0]

            return render_template('home.html', results=round(result, 2))

        except Exception as e:
            return f"Error: {str(e)}"

    else:
        return render_template('home.html')

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)