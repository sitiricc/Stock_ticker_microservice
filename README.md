# Stock Price Microservice

This is a microservice that uses Finnhub to pull price information for a particular stock.

## Instructions

To start using this microservice, you need a FREE API key from https://finnhub.io/

Once you receive one, create a .env file with the API key.

Install the requirements file.

Start your virtual environment to pull information from client_script and servicer_script and the Finnhub API.


## How to request data

Once the client_script.py file is initialized, text will pop up asking for a stock ticker. From there the user can enter the stock ticker of their choice and press Enter to send the request to the server.

A list of stock symbols can be found here:
https://stockanalysis.com/stocks/

An example call would be the user entering AAPL when prompted. This will send the request to get the information for the APPLE stock.

## How to receive data

Once you've entered a stock symbol and sent it to the server, the server will use the Finnhub API to pull the most recent pricing for the stock. The program will then display it to the user.


## UML Sequence Diagram

This diagram will show how to send and receive information.

![UML diagram](/images/UMLdiagram.png)