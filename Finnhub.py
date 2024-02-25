import zmq

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
    stock_ticker = input("Enter the stock symbol: ")
    current_price = get_stock_price(stock_ticker)
    print(f"Current price of {stock_ticker}: ${current_price}")
