from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("models/ridge.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")   # ✅ IMPORTANT

@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        data = [
            float(request.form.get("Temperature")),
            float(request.form.get("RH")),
            float(request.form.get("Ws")),
            float(request.form.get("Rain")),
            float(request.form.get("FFMC")),
            float(request.form.get("DMC")),
            float(request.form.get("ISI")),
            float(request.form.get("Classes")),
            float(request.form.get("Region"))
        ]

        final_input = scaler.transform([data])
        result = model.predict(final_input)[0]

        return render_template("home.html", results=round(result, 2))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)