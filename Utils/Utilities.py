import yfinance as yf
import pandas as pd
import numpy as np

def download_data(stocks, start_date, end_date):
    stock_data = {}

    for stock in stocks:
        ticker = yf.Ticker(stock)
        stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']

    return pd.DataFrame(stock_data)

def compute_return(data):
    #Normalization of returns such that they are comparable
    log_return = np.log(data/data.shift(1))
    return log_return[1:]