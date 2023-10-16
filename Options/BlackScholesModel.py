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
        print("D1 = {} and D2 = {}".format(d1,d2))
        return ((stock_price * stats.norm.cdf(d1)) -
                ((self.strike * exp(-self.rate * (self.expiry - time))) * stats.norm.cdf(d2)))

    def __compute_put_price(self, stock_price, time):
        d1 = self.__compute_d1(stock_price, time)
        d2 = self.__compute_d2(d1, time)
        print("D1 = {} and D2 = {}".format(d1,d2))
        return ((-stock_price * stats.norm.cdf(-d1)) +
                ((self.strike * exp(-self.rate * (self.expiry - time))) * stats.norm.cdf(-d2)))

    def compute_option_price(self, stock_price, time):
        if self.option_type == OptionType.CALL:
            return self.__compute_call_price(stock_price, time)
        return self.__compute_put_price(stock_price, time)

if __name__ == '__main__':
    call = BlackScholesModel(100, 0.20, 0.05, 1, OptionType.CALL)
    print("Call Option price is {:f}".format(call.compute_option_price(100,0)))

    put = BlackScholesModel(100, 0.20, 0.05, 1, OptionType.PUT)
    print("Put Option price is {:f}".format(put.compute_option_price(100,0)))







