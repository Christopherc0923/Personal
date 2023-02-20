from django.shortcuts import render
from .models import Stock
import requests
from django.conf import settings
import requests


# Create your views here.



def index(request):
    stocks = Stock.objects.all()
    return render(request, 'stock/index.html', {'stocks': stocks})

def info(request):
    return render(request, 'stock/info.html')

from datetime import datetime, timedelta

stocks = ['AAPL', 'GOOG', 'MSFT', 'SPY']

def update_stocks(time_period, stocks):
    Stock.objects.all().delete() # delete existing objects
    api_key = 'EEO2XGZO5KO1BBJI'
    for symbol in stocks:
        response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=full')
        data = response.json()
        try:
            daily_data = data['Time Series (Daily)']
            for date in daily_data:
                date_obj = datetime.strptime(date, '%Y-%m-%d')
                if (datetime.now() - date_obj).days > time_period:
                    break
                Stock.objects.create(
                    symbol=symbol,
                    name=data['Meta Data']['2. Symbol'],
                    date=datetime.strptime(date, '%Y-%m-%d'),
                    price=daily_data[date]['4. close']
                )
        except KeyError as e:
            print(f"Key error: {e}")
            print(data)

update_stocks(7, stocks)

import seaborn as sns
import matplotlib.pyplot as plt

def plot_stock_prices(symbol):
    plt.clf()
    stocks = Stock.objects.filter(symbol=symbol)
    prices = [stock.price for stock in stocks]
    dates = [stock.date for stock in stocks]

    sns.lineplot(x=dates, y=prices)
    plt.title(f"{symbol} Stock Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.savefig(f'stock/static/stock/{symbol}_plot.png')

for symbol in stocks:
    plot_stock_prices(symbol)