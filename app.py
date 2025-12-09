from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("addiction_model.pkl")
label_map = {0:"NORMAL USER", 1:"AT-RISK USER", 2:"MOBILE ADDICT"}

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[data["total"], data["social"], data["study"], data["entertainment"], data["gaming"]]])
    prediction = model.predict(features)[0]
    categories = {"Social Media":data["social"], "Study":data["study"], "Entertainment":data["entertainment"], "Gaming":data["gaming"]}
    most_used = max(categories, key=categories.get)
    return jsonify({"prediction":label_map[prediction], "most_used":most_used})

if __name__ == "__main__":
    app.run(debug=True)
