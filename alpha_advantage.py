import requests
import json
import datetime

def get_stock_data(symbol, interval, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def extract_current_price_and_time(data):
    if 'Time Series (5min)' in data:  # Adjust the key based on the interval used
        latest_data = data['Time Series (5min)']  # Adjust the key based on the interval used
        latest_timestamp = max(latest_data.keys())
        current_price = latest_data[latest_timestamp]['4. close']  # Adjust the key based on the data structure
        return current_price, latest_timestamp
    else:
        return None, None

if __name__ == "__main__":
    symbol = input("Enter stock symbol: ")
    interval = '5min'  # Choose the desired interval, e.g., 1min, 5min, 15min, 30min, 60min
    api_key = 'UVKHRIM8YJ071AM7'  # Replace with your actual API key

    stock_data = get_stock_data(symbol, interval, api_key)
    price, timestamp = extract_current_price_and_time(stock_data)
    
    if price is not None and timestamp is not None:
        print(f"Current price of {symbol}: ${price} as of {timestamp}")
    else:
        print(f"Failed to retrieve data for {symbol}")
