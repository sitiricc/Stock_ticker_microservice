import os
import sys
import zmq

# Append the parent directory of client_script.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def get_stock_price(stock_ticker):
    """Send request for stock ticker to server and receive current stock price."""
    socket.send_string(stock_ticker)

    # Receive current stock price from server
    current_price = socket.recv_string()
    return current_price


if __name__ == "__main__":
    # Get the reply.
    stock_ticker = input("What stock ticker did you want the price of?: ")
    current_price = get_stock_price(stock_ticker)
    print("This program takes an input of a stock ticker and provides the current price.")
    print(f"Current price of {stock_ticker}: ${current_price}")
