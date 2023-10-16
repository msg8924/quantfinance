from scipy.stats import norm
from numpy import sqrt
class ValueAtRiskCalculator:

    def __init__(self, S, mu, sigma, c, n):
        self.S = S
        self.mu = mu
        self.sigma = sigma
        self.c = c
        self.n = n

    def compute_value_at_risk(self):
        return self.S * (self.mu * self.n - self.sigma * sqrt(self.n) * norm.ppf(1-self.c))



if __name__ == '__main__':
    calculator = ValueAtRiskCalculator(1e6, 0.01, 0.0005,0.99, 10)
    print("With {:.2f} confidence, the portfolio will not lose more than ${:.2f} over the"
          " next {} day(s)".format(calculator.c, calculator.compute_value_at_risk(), calculator.n))