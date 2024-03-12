from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

import finnhub
from dotenv import load_dotenv
import os

app = Flask(__name__)

CORS(app)

load_dotenv()
api_key = os.getenv('API_KEY')
finnhub_client = finnhub.Client(api_key=api_key)

def get_stock_price(stock_ticker):
    """Get current data for stock. """
    data = finnhub_client.quote(stock_ticker)
    print(data)
    current_price = data['c']
    timestamp = data['t']
    timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    print(current_price, timestamp)
    return timestamp, current_price

@app.route('/stock_price', methods=['GET'])
def stock_price():
    symbol = request.args.get('q')
    if symbol:
        timestamp, price = get_stock_price(symbol)
        if price == 0 and str(timestamp) == '1969-12-31':
            return jsonify({"error": "Failed to retrieve data for symbol"}), 404
        else:
            return jsonify({"timestamp": timestamp, "price": price}), 200  
    else:
        return jsonify({"error": "No symbol provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5555)