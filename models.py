import pandas as pd
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

API_KEY = 'Zdc_5W8HMS73_TTC_KFX6vdoZTl1H4bU'
BASE_URL = 'https://api.polygon.io/v2/aggs/ticker'

# Fetch stock data from Polygon API
def fetch_stock_data(symbol, date):
    params = {
        'range': '1',
        'multiplier': '1',
        'timespan': 'day',
        'from': date,
        'to': date,
        'apiKey': API_KEY
    }
    response = requests.get(f"{BASE_URL}/{symbol}/range/1/day/{date}/{date}", params=params)

    # Check if we have valid data
    if response.status_code != 200:
        print(f"Error fetching data for {symbol}: {response.json().get('error', 'Unknown error')}")
        return None

    # Extract the relevant data
    data = response.json()
    stock_data = []
    for result in data.get('results', []):
        stock_data.append({
            'Date': pd.to_datetime(result['t'], unit='ms'),  # Convert timestamp to datetime
            'Close': result['c']  # Closing price
        })

    return pd.DataFrame(stock_data)

# Train a linear regression model for stock prediction
def train_model(df):
    df = df[['Date', 'Close']].copy()
    df['Date'] = pd.to_numeric(df['Date'].dt.strftime('%Y%m%d'))  # Convert date to numeric
    X = df['Date'].values.reshape(-1, 1)
    y = df['Close'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, X_test, y_test

# Function to predict future stock prices
def predict_prices(df):
    model, X_test, y_test = train_model(df)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Create a DataFrame with predictions and actuals
    predictions = pd.DataFrame({
        'Date': pd.to_datetime(X_test.flatten(), format='%Y%m%d'),
        'Actual': y_test,
        'Predicted': y_pred
    })

    return predictions
