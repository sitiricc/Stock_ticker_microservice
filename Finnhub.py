import finnhub

finnhub_client = finnhub.Client(api_key="cnd8vupr01qr85dtlqp0cnd8vupr01qr85dtlqpg")

def get_current_price(symbol):
    """Get current data for stock. """
    data = finnhub_client.quote(symbol)
    return data['c']

if __name__ == "__main__":
    symbol = input("Enter the stock symbol: ")
    current_price = get_current_price(symbol)
    print(f"Current price of {symbol}: ${current_price}")