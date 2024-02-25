import yfinance as yf
import datetime


def price_conversion(amount):
    """Converts amount into US dollars and cents."""
    currency='${:>,.2f}'.format(amount)
    return currency


def get_stock_price(stock_ticker):
    """Gets stock price for given ticker."""
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    data = yf.Ticker(stock_ticker)
    data = data.history(start="2010-01-01", end=now)
    if not data.empty:
        current_price = data['Close'].iloc[-1]
        formatted_price= price_conversion(current_price)
        return now, formatted_price
    else:
        return None, None
    

if __name__ == '__main__':
    symbol = input("Enter stock ticker symbol: ")
    timestamp, price = get_stock_price(symbol)
    if price is not None:
        print(f"Current price of {symbol}: {price} as of {timestamp}")
    else:
        print(f"Failed to retrieve data for {symbol}")
