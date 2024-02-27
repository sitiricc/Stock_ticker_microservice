from flask import Flask, render_template, request
from client_script import get_stock_price



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    stock_ticker = request.form['stock_ticker']
    current_price = get_stock_price(stock_ticker)
    return render_template('result.html', stock_ticker=stock_ticker, current_price=current_price)

if __name__ == '__main__':
    app.run(debug=True)
