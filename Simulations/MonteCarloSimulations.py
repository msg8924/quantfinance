import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MonteCarloSimulations:

    #simulate a yearly stock price movement over multiple simulations
    def __init__(self, initial_price, mu, sigma, dt, no_of_simulations=1000, no_of_realizations=252):
        self.initial_price = initial_price
        self.no_of_simulations = no_of_simulations
        self.no_of_realizations = no_of_realizations
        self.mu = mu
        self.sigma = sigma
        self.dt = dt


    def run_simulation(self):
        np.random.seed(43)
        simulations = []
        for _ in range(self.no_of_simulations):
            realizations = [self.initial_price]
            for _ in range(self.no_of_realizations):
                new_stock_price = realizations[-1]*np.exp(((self.mu - 0.5 * self.sigma**2)*self.dt) + (self.sigma*np.random.normal(0, np.sqrt(self.dt))))
                realizations.append(new_stock_price)
            simulations.append(realizations)

        simulations = pd.DataFrame(simulations).T
        return simulations

    def plot(self, data):
        plt.plot(data)
        plt.show()


if __name__ == '__main__':
    simulation = MonteCarloSimulations(50, 0.0002, 0.01, 1)
    data = simulation.run_simulation()
    simulation.plot(data)

    last_line = data.tail(1)

    print(last_line)