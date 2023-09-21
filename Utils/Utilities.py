import yfinance as yf
import pandas as pd
import numpy as np

def download_data(stocks, start_date, end_date, resample = None):
    stock_data = {}

    for stock in stocks:
        ticker = yf.download(stock, start_date, end_date)
        stock_data[stock] = ticker['Adj Close']

    if resample == None:
        return pd.DataFrame(stock_data)
    return pd.DataFrame(stock_data).resample('M').last()

def compute_return(data):
    #Normalization of returns such that they are comparable
    log_return = np.log(data/data.shift(1))
    return log_return[1:]