from flask import Flask, request, jsonify, render_template
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API with rule-based categorization
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Extract category hours
    social = data.get("social", 0)
    study = data.get("study", 0)
    entertainment = data.get("entertainment", 0)
    gaming = data.get("gaming", 0)

    # Total usage automatically calculated
    total = social + study + entertainment + gaming

    # Rule-based categorization
    if total <= 4:
        prediction = "NORMAL USER"
    elif total <= 8:
        prediction = "AT-RISK USER"
    else:
        prediction = "MOBILE ADDICT"

    # Determine most used category
    categories = {"Social Media": social, "Study": study, "Entertainment": entertainment, "Gaming": gaming}
    most_used = max(categories, key=categories.get)

    # Return JSON response
    return jsonify({
        "prediction": prediction,
        "most_used": most_used,
        "total": total
    })


if __name__ == "__main__":
    app.run(debug=True)
