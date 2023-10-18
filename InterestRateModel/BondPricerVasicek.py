import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def run_simulations(r0, kappa, theta, sigma, T=1.0, simulations=1000, points=200):
    dt = T/float(points)
    simulation_data = []
    for _ in range(simulations):
        rates = [r0]
        for _ in range(points):
            dr = (kappa * (theta - rates[-1]) * dt) + (sigma * np.random.normal(0, np.sqrt(dt)))
            rates.append(rates[-1]+dr)

        simulation_data.append(rates)

    simulation_data = pd.DataFrame(simulation_data).T
    integral_sum = simulation_data.sum() * dt
    return np.mean(np.exp(-integral_sum))


if __name__ == '__main__':
    simulated_rate = run_simulations(0.1, 0.3, 0.3, 0.03)
    print('Bond price based on Monte Carlo Simulation is {0:.4f}'.format(1000 * simulated_rate))
    print("Simulated Rate is {0:.4f}".format(simulated_rate))