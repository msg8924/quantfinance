from Utils.Utilities import download_data
from Utils.Utilities import compute_return
from Utils.Statistics import compute_covariance
from Utils.Statistics import compute_variance
from Utils.Statistics import compute_expected_value
import numpy as np

RISK_FREE_RATE = 0.05

def compute_expected_return_market(log_returns,market_ticker='SPY'):
    market_log_returns = log_returns.loc[:, data.columns == market_ticker].values
    return compute_expected_value(market_log_returns)

def compute_expected_return(beta,expected_return_market,risk_free_rate):
    return risk_free_rate + (beta * (expected_return_market - risk_free_rate))


def compute_betas(log_returns, tickers):
    betas = {}
    tickers.remove('SPY')
    for ticker in tickers:
        betas[ticker] = compute_beta(log_returns, ticker)
    return betas

def compute_beta(log_returns, stock_ticker, market_ticker='SPY'):
    stock_log_returns = log_returns.loc[:, data.columns == stock_ticker].values
    market_log_returns = log_returns.loc[:, data.columns == market_ticker].values
    covariance = compute_covariance(stock_log_returns, None, market_log_returns, None)[0]
    variance = compute_variance(market_log_returns, None)
    return covariance / variance

if __name__ == '__main__':
    tickers = ['AAPL','JPM','JNJ','SPY']
    weights = [0.25] * 3
    start_date = '2023-01-01'
    end_date = '2023-09-14'
    data = download_data(tickers, start_date, end_date)
    log_returns = compute_return(data)
    betas = compute_betas(log_returns,tickers)
    expected_return_market = compute_expected_return_market(log_returns)
    beta_portfolio = np.dot(np.array(list(betas.values())), np.array(weights).T)
    print("Portfolio's beta is {0:.5f}".format(beta_portfolio))
    for beta in betas:
        expected_return = compute_expected_return(betas[beta],expected_return_market, RISK_FREE_RATE)
        print("Ticker {0} has a beta of {1:.5f} and has a return of {2:.5f}".format(beta, betas[beta], expected_return * 100))








