from numpy.random import normal
import matplotlib.pyplot as plt
import numpy as np

def vasicek_model(initial_r, kappa, theta,  sigma, T=1.0, N=10000 ):
    dt = T/float(N)
    t = np.linspace(0,T, N+1)
    rates = [initial_r]

    for _ in range(N):
        dr = (kappa * (theta - rates[-1]) * dt) + (sigma * normal(0, np.sqrt(dt)))
        rates.append(rates[-1]+dr)

    return t, rates

def plot_model(t, rates):
    plt.plot(t,rates)
    plt.xlabel("t")
    plt.ylabel("r(t)")
    plt.title("Vasicek Model")
    plt.show()

if __name__ == "__main__":
    t, rates = vasicek_model(-1.3,0.9,1.5,0.25)
    plot_model(t,rates)