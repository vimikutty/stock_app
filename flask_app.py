# app.py
from flask import Flask, render_template, jsonify
from ai_predictor import get_stock_prediction  # Import your AI prediction function

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    # Get stock prediction data
    stock_info = get_stock_prediction()  # Returns current, predicted, and historical data
    return render_template("index.html", stock_info=stock_info)

# API endpoint for predictions (optional, useful if you want JS to fetch dynamically)
@app.route("/api/predictions")
def api_predictions():
    return jsonify(get_stock_prediction())

# Login page
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

