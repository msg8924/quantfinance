import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1.0  # Time horizon
N = 1000  # Number of time steps
dt = T / N  # Time step

# Generate Brownian motion path
t = np.linspace(0.0, T, N+1)
W = np.cumsum(np.sqrt(dt) * np.random.randn(N+1))

# Select a time point
t_selected = 0.5

# Find the index corresponding to the selected time point
index_selected = int(t_selected / T * N)

# Simulate future path
s = 0.2  # Future time
s_index = int(s / T * N)
future_path = np.concatenate(([W[index_selected]], W[index_selected + 1:index_selected + s_index]))

# Markov Property Visualization (memory less)
# Markov Property
# A stochastic process (such as a sequence of random variables) exhibits the Markov property if the future behavior of
# the process, given its history up to a certain time, only depends on the current state and is independent of the past.
# conditional distribution of the process B(t) given information until s < t is dependent of B(s)
#The conditional distribution of a random variable describes the probability distribution of that variable
# given certain information or conditions.
# It provides information about how the variable's values are distributed within a specific context or condition.
# Example of this would be by letting X be Heights and Y be gender.
# Thus P(X | Y = male) would describe how heights are distributed among males.
plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.plot(t, W, label="Path")
plt.plot([t_selected, t_selected + s], [W[index_selected], future_path[-1]], 'ro-', label="Future Path")
plt.title("Markov Property Visualization (memory less) - future state only depends on current state and is independent of past")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()

# Martingale Property Visualization
# A stochastic process is a martingale if
# 1) it is integrable E[|B(t)|] < inf and
# 2) Conditional Expectation: E[B(t) | F(s)] = B(s) for s < t
# given information s < t, the conditional expectation of B(t) is B(s)
# focuses on the conditional expectations of future values given the available information
# Conditional expectation, on the other hand, is a numerical summary of a random variable's expected value given certain
# information or conditions. It represents the average or expected value of a random variable under a specific condition.
# Example of this would be by letting X be Income and Y be Education.
# E[X| Y = college degree) would represent the average income of individuals with a college degree.
plt.subplot(122)
plt.plot(t, W, label="Path")
plt.plot([t_selected, t_selected + s], [W[index_selected], W[index_selected]], 'ro-', label="Conditional Expectation")
plt.title("Martingale Property Visualization (best estimate of current is immediate past)")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()

plt.tight_layout()
plt.show()
