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
    betas_ols = {}
    betas_gd = {}
    tickers.remove('SPY')
    for ticker in tickers:
        print("Ticker {0}'s betas:".format(ticker))
        covariance_beta = compute_beta(log_returns, ticker)
        betas[ticker] =covariance_beta
        ols, gd = compute_beta_regression(log_returns, ticker, 'SPY', covariance_beta, 1)
        betas_ols[ticker] = ols[1]
        betas_gd[ticker] = gd[1]
        print()
    return betas, betas_ols, betas_gd


def compute_beta(log_returns, stock_ticker, market_ticker='SPY'):
    stock_log_returns = np.concatenate(log_returns.loc[:, data.columns == stock_ticker].values)
    market_log_returns = np.concatenate(log_returns.loc[:, data.columns == market_ticker].values)
    covariance = compute_covariance(stock_log_returns, None, market_log_returns, None)
    variance = compute_variance(market_log_returns, None)
    covariance_matrix = np.cov(stock_log_returns, market_log_returns)
    print("Beta - Covariance Matrix method: {0:.5f}".format(covariance_matrix[0, 1] / covariance_matrix[1, 1]))
    return covariance / variance

def compute_beta_regression(log_returns, stock_ticker, market_ticker='SPY', initial_w= 0, initial_b= 0):
    stock_log_returns = np.concatenate(log_returns.loc[:, data.columns == stock_ticker].values)
    market_log_returns = np.concatenate(log_returns.loc[:, data.columns == market_ticker].values)
    reg = UnivariateLinearRegression()
    intercept_ols, beta_ols = reg.ols_estimate_coefficients(market_log_returns, stock_log_returns)
    print("Estimated coefficients using OLS: b_0 = {0:.5f} & b_1 = {1:.5f}".format(intercept_ols, beta_ols))
    intercept_gd, beta_gd = reg.fit(market_log_returns, stock_log_returns, alpha=0.01, num_iters=1000, threshold=0.0001,
                                    initial_w=initial_w, initial_b=initial_b, print_statement=False)
    print("Estimated coefficients using Gradient Descent: b_0 = {0:.5f} & b_1 = {1:.5f}".format(intercept_gd, beta_gd))
    return (intercept_ols, beta_ols),(intercept_gd, beta_gd)

if __name__ == '__main__':
    tickers = ['AAPL', 'GS', 'SPY']
    num_stocks = (len(tickers) - 1)
    weights = [1/num_stocks] * num_stocks
    start_date = '2018-09-14'
    end_date = '2023-09-14'
    data = download_data(tickers, start_date, end_date, 'M')
    log_returns = compute_return(data)
    betas, betas_ols, betas_gd = compute_betas(log_returns, tickers)
    portfolio_beta = compute_portfolio_beta(betas, weights)
    print("Portfolio's beta using Covariance is {0:.5f}".format(portfolio_beta))
    portfolio_beta_ols = compute_portfolio_beta(betas_ols, weights)
    print("Portfolio's beta using OLS  is {0:.5f}".format(portfolio_beta_ols))
    portfolio_beta_gd = compute_portfolio_beta(betas_gd, weights)
    print("Portfolio's beta using GD  is {0:.5f}".format(portfolio_beta_gd))
    print()
    expected_return_market = compute_expected_return_market(log_returns)
    for beta in betas:
        expected_return = compute_expected_return(betas[beta], expected_return_market, RISK_FREE_RATE)
        print("Ticker {0} has a Covariance beta of {1:.5f} and has a return of {2:.5f}".format(beta, betas[beta], expected_return))

        expected_return = compute_expected_return(betas_ols[beta], expected_return_market, RISK_FREE_RATE)
        print("Ticker {0} has a OLS beta of {1:.5f} and has a return of {2:.5f}".format(beta, betas_ols[beta], expected_return))

        expected_return = compute_expected_return(betas_gd[beta], expected_return_market, RISK_FREE_RATE)
        print("Ticker {0} has a GD beta of {1:.5f} and has a return of {2:.5f}".format(beta, betas_gd[beta], expected_return))
        print()


