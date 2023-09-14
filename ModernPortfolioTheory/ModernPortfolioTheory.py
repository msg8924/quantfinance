import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

NO_OF_TRADING_DAYS = 252
NO_OF_PORTFOLIOS = 10000

def download_data(stocks, start_date, end_date):
    stock_data = {}

    for stock in stocks:
        ticker = yf.Ticker(stock)
        stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']

    return pd.DataFrame(stock_data)

def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()

def compute_return(data):
    #Normalization of returns such that they are comparable
    log_return = np.log(data/data.shift(1))
    return log_return[1:]

def compute_statistics(returns):
    #Annualize the returms
    print(returns.mean() * NO_OF_TRADING_DAYS)
    print(returns.cov() * NO_OF_TRADING_DAYS)

def compute_mean_variance(returns, weights, show = False):
    portfolio_mean = np.sum(returns.mean()*weights) * NO_OF_TRADING_DAYS
    portfolio_variance = np.dot(weights.T, np.dot(returns.cov()*NO_OF_TRADING_DAYS, weights))
    portfolio_std_dev = np.sqrt(portfolio_variance)
    if show :
        print("Portfolio Mean: %.2f" %  portfolio_mean)
        print("Portfolio Variance: %.2f"% portfolio_variance)
        print("Portfolio Std Dev: %.2f" % portfolio_std_dev)
    return portfolio_mean, portfolio_variance


def generate_portfolios(returns):
    portfolio_means = []
    portfolio_variance = []
    portfolio_weights = []
    no_of_stocks = len(returns.columns)

    for _ in range(NO_OF_PORTFOLIOS):
        w = np.random.random(no_of_stocks)
        w /= np.sum(w)
        portfolio_weights.append(w)
        port_mean, port_variance = compute_mean_variance(returns, w)
        portfolio_means.append(port_mean)
        portfolio_variance.append(port_variance)

    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_variance)


def show_portfolios(returns, variance):
    plt.figure(figsize=(10,6))
    volatilities = np.sqrt(variance)
    plt.scatter(volatilities,returns, c=returns/volatilities,marker ='o' )
    plt.grid(True)
    plt.xlabel('Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()

if __name__ == '__main__':
    stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'DB']
    weights = [0.20,0.20,0.20,0.20,0.20]
    start_date = '2023-01-01'
    end_date = '2023-09-13'
    data = download_data(stocks, start_date, end_date)
    #show_data(data)
    log_returns = compute_return(data)
    # show_data(log_returns)
    compute_statistics(log_returns)
    compute_mean_variance(log_returns, np.array(weights), True)
    print(log_returns.mean())
    weights, mean, variance = generate_portfolios(log_returns)
    show_portfolios(mean,variance)