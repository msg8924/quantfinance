import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random

def generate_random_part(sigma, S, dt):
    return S * random.normal(0,np.sqrt(dt)) * sigma

def generate_drift_part(sigma, S, dt):
    return S * sigma * dt

def generate_geometric_random_walk(S, dt, sigma, n=1000):
    #dS = sigmaS.dt + sigmaSdW
    t = np.linspace(0,n,n+1)
    dS = np.zeros(n+1)
    dS[0] = S
    for i in range(1, n+1):
        dS[i] = dS[i-1] + (generate_drift_part(sigma,S,dt) + generate_random_part(sigma,S,dt))
    #dS[1:n+1] = np.cumsum((generate_drift_part(sigma,S,dt) + generate_random_part(sigma,S,dt),n))

    return t, dS


def plot_geometric_random_walk(t, dS):
    plt.plot(t,dS)
    plt.xlabel("time")
    plt.ylabel("S")
    plt.show()


def simulate_geometric_random_walk(S0, T=2, N=1000, mu=0.01, sigma=0.05):

    dt = T/N
    t = np.linspace(0, T, N)
    # standard normal distribution N(0,1)
    W = np.random.standard_normal(size=N)
    # N(0,dt) = sqrt(dt) * N(0,1)
    W = np.cumsum(W) * np.sqrt(dt)
    X = (mu - 0.5 * sigma ** 2) * t + sigma * W
    S = S0 * np.exp(X)

    return t, S

if __name__ == '__main__':
    t, S = generate_geometric_random_walk(100,0.002, 0.01)
    plot_geometric_random_walk(t,S)
    t, S = simulate_geometric_random_walk(100)
    plot_geometric_random_walk(t,S)