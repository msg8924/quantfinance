from scipy.stats import norm
from numpy import sqrt
from numpy import random
from numpy import exp
from numpy import sort
from numpy import percentile

class ValueAtRiskCalculator:

    def __init__(self, position, mu, sigma, c, n):
        self.position = position
        self.mu = mu
        self.sigma = sigma
        self.c = c
        self.n = n

    def compute_value_at_risk(self):
        return self.position * (self.mu * self.n - self.sigma * sqrt(self.n) * norm.ppf(1-self.c))

    def simulate(self, iterations, initial_stock_price):
        W = random.normal(0,1,[1,iterations])
        stock_prices = initial_stock_price * exp(((self.mu - self.sigma**2/2)*self.n) + (self.sigma * sqrt(self.n) *W))
        stock_prices = sort(stock_prices)
        stock_price = percentile(stock_prices, (1-self.c) * 100)
        qty = self.position / initial_stock_price
        return abs(qty * (initial_stock_price - stock_price))

if __name__ == '__main__':
    calculator = ValueAtRiskCalculator(1e6, 0.05, 0.005,0.99, 10)
    print("With {:.2f} confidence, the portfolio will not lose more than ${:.2f} over the"
          " next {} day(s)".format(calculator.c, calculator.compute_value_at_risk(), calculator.n))
    print("With {:.2f} confidence, the portfolio will not lose more than ${:.2f} over the"
          " next {} day(s)".format(calculator.c, calculator.simulate(100000,100), calculator.n))