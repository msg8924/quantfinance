import pandas as pd

import MonteCarloSimulations as simulations
from enum import Enum
import numpy as np

class OptionType(Enum):
    CALL = 1
    PUT = 2
class OptionsPricingMonteCarlo:
    def __init__(self, risk_free_rate, strike, initial_price, mu, sigma, dt, no_of_simulations=1000, no_of_realizations=252):
        self.risk_free_rate = risk_free_rate
        self.strike = strike
        self.time = dt
        self.simulation = simulations.MonteCarloSimulations(initial_price, mu, sigma, dt, no_of_simulations, no_of_realizations)
        self.data = self.simulation.run_simulation()

    def __compute_call_payout(self, price):
        return max(self.strike - price.values[0],0)

    def __compute_put_payout(self, price):
        return max(price.values[0] - self.strike,0)

    def __compute_payout(self, option_type: OptionType, data):
        if option_type == OptionType.CALL:
            payout = data.apply(self.__compute_call_payout)
        else:
            payout = data.apply(self.__compute_put_payout)

        print("Average Stock Price is {:.5f}".format(np.average(data)))
        print("Average Payout is {:.5f}".format(np.average(payout)))
        return np.average(payout) * np.exp(-self.risk_free_rate * self.time)


    def compute_call_option_price(self):
        return self.__compute_payout(OptionType.CALL, self.data.tail(1))

    def compute_put_option_price(self):
        return self.__compute_payout(OptionType.PUT, self.data.tail(1))


if __name__ == '__main__':
    pricer = OptionsPricingMonteCarlo(0.05, 9, 11, 0.0002, 0.05, 1,no_of_simulations=1000)
    print
    print("Call price is {:.5f}".format(pricer.compute_call_option_price()))
    print("Put price is {:.5f}".format(pricer.compute_put_option_price()))

