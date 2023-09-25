import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random

def generate_weiner_process(dt=0.01, x0 = 0, n=1000):
    W = np.zeros(n+1)
    t = np.linspace(x0,n, n+1)

    W[1:n+1] = np.cumsum(random.normal(0,np.sqrt(dt),n))
    return W, t

def plot_weiner_proces(W,t):
    plt.plot(t,W)
    plt.xlabel('T(t)')
    plt.ylabel('W(t)')
    plt.title("Weiner Process Realization")
    plt.show()

if __name__ == '__main__':
    W, t = generate_weiner_process()
    plot_weiner_proces(W,t)