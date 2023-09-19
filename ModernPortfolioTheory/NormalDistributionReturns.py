import numpy as np
import Utils.Utilities as utils
import matplotlib.pyplot as plt
from scipy.stats import norm

def get_data(tickers, start_date = '2023-01-01', end_date='2023-09-01'):
    return utils.download_data(tickers, start_date=start_date,end_date=end_date)

def show_plot(stock_data):
    plt.hist(stock_data, bins=300)
    stock_variance = stock_data.var()
    stock_mean = stock_data.mean()
    sigma = np.sqrt(stock_variance)
    x = np.linspace(stock_mean - 3 * sigma, stock_mean + 3 * sigma, 100)
    plt.plot(x, norm.pdf(x, stock_mean, sigma))
    plt.show()

if __name__ == '__main__':
    ticker = 'IBM'
    data = get_data([ticker],'2010-01-01', '2020-01-01')
    log_returns = utils.compute_return(data)
    ticker_log_returns = np.concatenate(log_returns.loc[:, data.columns == ticker].values)
    show_plot(ticker_log_returns)
