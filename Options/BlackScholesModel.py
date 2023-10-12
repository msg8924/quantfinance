from scipy import stats
from numpy import log, exp, sqrt
from enum import Enum

class OptionType(Enum):
    CALL = 1
    PUT = 2

class BlackScholesModel:
    def __init__(self, strike, sigma, rate, expiry, option_type: OptionType):
        self.option_type = option_type
        self.strike = strike
        self.sigma = sigma
        self.rate = rate
        self.expiry = expiry

    def __compute_d1(self, stock_price, time):
        return ((log(stock_price/self.strike) + (self.rate + (self.sigma**2)/2)*(self.expiry-time))
                /(self.sigma*sqrt(self.expiry-time)))
    def __compute_d2(self, d1, time):
        return d1 - self.sigma*sqrt(self.expiry-time)

    def __compute_call_price(self, stock_price, time):
        d1 = self.__compute_d1(stock_price, time)
        d2 = self.__compute_d2(d1,time)
        return ((stock_price * stats.norm.cdf(d1)) -
                ((self.strike * exp(-1 * self.rate * (self.expiry - time))) * stats.norm.cdf(d2)))

    def __compute_put_price(self, stock_price, time):
        d1 = self.__compute_d1(stock_price, time)
        d2 = self.__compute_d2(d1, time)
        return ((-1 * stock_price * stats.norm.cdf(-1 * d1)) -
                ((self.strike * exp(-1 * self.rate * (self.expiry - time))) * stats.norm.cdf(-1 * d2)))

    def compute_option_price(self, stock_price, time):
        if self.option_type == OptionType.CALL:
            return self.__compute_call_price(stock_price, time)
        return self.__compute_put_price(stock_price, time)


if __name__ == '__main__':
    bsm = BlackScholesModel(100, 0.50, 0.50, 10, OptionType.CALL)
    print(bsm.compute_option_price(120,5))








