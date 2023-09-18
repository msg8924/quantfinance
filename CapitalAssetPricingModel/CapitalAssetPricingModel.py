from Utils.Utilities import download_data
from Utils.Utilities import compute_return
from Utils.Statistics import compute_covariance
from Utils.Statistics import compute_variance
from Utils.Statistics import compute_expected_value
from DataScience.UnivariateLinearRegression import UnivariateLinearRegression
import numpy as np

RISK_FREE_RATE = 0.05
MONTHS_IN_YEAR = 12

def compute_expected_return_market(log_returns, market_ticker='SPY'):
    market_log_returns = log_returns.loc[:, data.columns == market_ticker].values
    return compute_expected_value(market_log_returns)


def compute_expected_return(beta, expected_return_market, risk_free_rate):
    return risk_free_rate + (beta * (expected_return_market * MONTHS_IN_YEAR - risk_free_rate))


def compute_portfolio_beta(betas, weights):
    stock_betas = np.array(list(betas.values()))
    portfolio_beta = np.dot(stock_betas, np.array(weights).T)
    return portfolio_beta


def compute_betas(log_returns, tickers):
    betas = {}
    tickers.remove('SPY')
    for ticker in tickers:
        betas[ticker] = compute_beta(log_returns, ticker)
        compute_beta_regression(log_returns, ticker)
    return betas


def compute_beta(log_returns, stock_ticker, market_ticker='SPY'):
    stock_log_returns = np.concatenate(log_returns.loc[:, data.columns == stock_ticker].values)
    market_log_returns = np.concatenate(log_returns.loc[:, data.columns == market_ticker].values)
    covariance = compute_covariance(stock_log_returns, None, market_log_returns, None)
    variance = compute_variance(market_log_returns, None)
    covariance_matrix = np.cov(stock_log_returns, market_log_returns)
    print("Beta - Covariance Matrix method: {0:.5f}".format(covariance_matrix[0, 1] / covariance_matrix[1, 1]))
    return covariance / variance

def compute_beta_regression(log_returns, stock_ticker, market_ticker='SPY'):
    stock_log_returns = np.concatenate(log_returns.loc[:, data.columns == stock_ticker].values)
    market_log_returns = np.concatenate(log_returns.loc[:, data.columns == market_ticker].values)
    reg = UnivariateLinearRegression(iterations=1000, learning_rate=0.01)
    print(reg.estimate_coefficients(market_log_returns, stock_log_returns))

if __name__ == '__main__':
    tickers = ['AAPL', 'SPY']
    num_stocks = (len(tickers) - 1)
    weights = [1/num_stocks] * num_stocks
    start_date = '2023-01-01'
    end_date = '2023-09-14'
    data = download_data(tickers, start_date, end_date, 'M')
    log_returns = compute_return(data)
    betas = compute_betas(log_returns, tickers)
    portfolio_beta = compute_portfolio_beta(betas, weights)
    print("Portfolio's beta is {0:.5f}".format(portfolio_beta))
    expected_return_market = compute_expected_return_market(log_returns)
    for beta in betas:
        expected_return = compute_expected_return(betas[beta], expected_return_market, RISK_FREE_RATE)
        print("Ticker {0} has a beta of {1:.5f} and has a return of {2:.5f}".format(beta, betas[beta], expected_return))


