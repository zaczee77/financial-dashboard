import requests
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

def fetch_stock_data(symbol):
    API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=compact'
    
    response = requests.get(url)
    data = response.json()
    
    if 'Time Series (Daily)' not in data:
        return None, data.get('Note', 'No data available.')

    prices = data['Time Series (Daily)']
    dates = []
    close_prices = []

    for date, metrics in sorted(prices.items()):
        dates.append(date)
        close_prices.append(float(metrics['4. close']))

    return {'dates': dates, 'close': close_prices}, None

def fetch_news(symbol):
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    url = f'https://newsapi.org/v2/everything?q={symbol}&apiKey={NEWS_API_KEY}'
    
    response = requests.get(url)
    news_data = response.json()

    if news_data.get('status') != 'ok':
        return None, news_data.get('message', 'Error fetching news.')

    articles = [article['title'] for article in news_data.get('articles', [])[:5]]
    return articles, None

def predict_stock_price(prices):
    # Preparing data for linear regression
    df = pd.DataFrame({'Price': prices})
    df['Day'] = df.index + 1  # Create a day feature
    X = df[['Day']]
    y = df['Price']

    # Train linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict the next price (next day)
    next_day = np.array([[len(prices) + 1]])
    predicted_price = model.predict(next_day)

    return predicted_price[0]
