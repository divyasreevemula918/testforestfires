from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("models/ridge.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        try:
            temperature = float(request.form.get("Temperature"))
            rh = float(request.form.get("RH"))
            ws = float(request.form.get("Ws"))
            rain = float(request.form.get("Rain"))
            ffmc = float(request.form.get("FFMC"))
            dmc = float(request.form.get("DMC"))
            isi = float(request.form.get("ISI"))
            classes = float(request.form.get("Classes"))
            region = float(request.form.get("Region"))

            data = np.array([[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]])
            scaled_data = scaler.transform(data)
            result = model.predict(scaled_data)[0]

            return render_template("home.html", results=round(result, 2))
        except Exception as e:
            return render_template("home.html", results=f"Error: {e}")

    return render_template("home.html", results=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)