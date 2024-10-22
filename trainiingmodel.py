# trading_model.py
import numpy as np

def random_prediction(stock_name):
    # For demonstration, generate a random prediction
    return np.random.choice(['Buy', 'Hold', 'Sell'])

def get_real_time_news():
    # Placeholder: In real scenario, fetch data from your news API
    return [
        "Breaking: Major stock market changes",
        "Update: Tech stocks rally amid earnings season",
        "Insight: Analysts predict market recovery"
    ]
