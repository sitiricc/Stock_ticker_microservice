import zmq
import finnhub
import os
from dotenv import load_dotenv
import datetime

# https://finnhub.io/docs/api/websocket-trades
# https://zeromq.org/get-started/?language=python#


# API key and code.
load_dotenv()
api_key = os.getenv('API_KEY')
finnhub_client = finnhub.Client(api_key=api_key)


context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

load_dotenv()
api_key= os.getenv('API_KEY')

def get_current_price(stock_ticker):
    """Get current data for stock. """
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    data = finnhub_client.quote(stock_ticker)
    return data['c']



while True:
    #  Wait for next request from client
    message = socket.recv_string()
    print(f"Received request: {message}")
    
    #  Send reply back to client
    stock_ticker = message
    current_price = get_current_price(stock_ticker)
    socket.send_string(str(current_price))