# ai_predictor.py
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def get_stock_prediction(ticker="AAPL", period="60d", interval="1d"):
    # Download historical data
    data = yf.download(ticker, period=period, interval=interval)
    data = data[['Close']]

    # Add prediction column
    data['Prediction'] = data['Close'].shift(-1)

    # Prepare training data
    X = np.array(data[['Close']][:-1])
    y = np.array(data['Prediction'][:-1])

    # Train linear regression
    model = LinearRegression()
    model.fit(X, y)

    # Predict next day's price
    last_price = np.array([[data['Close'].iloc[-1]]])
    predicted_price = model.predict(last_price)[0][0]

    # Prepare data to return (dates + prices)
    historical_data = [{"date": str(d.date()), "price": float(p)} for d, p in zip(data.index, data['Close'])]
    
    return {
        "current_price": float(last_price[0][0]),
        "predicted_price": float(predicted_price),
        "historical_data": historical_data
    }

