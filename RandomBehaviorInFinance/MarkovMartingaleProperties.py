import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1.0  # Time horizon
N = 1000  # Number of time steps
dt = T / N  # Time step

# Generate Brownian motion path
t = np.linspace(0.0, T, N+1)
W = np.cumsum(np.sqrt(dt) * np.random.randn(N))

# Select a time point
t_selected = 0.5

# Find the index corresponding to the selected time point
index_selected = int(t_selected / T * N)

# Simulate future path
s = 0.2  # Future time
s_index = int(s / T * N)
future_path = np.concatenate(([W[index_selected]], W[index_selected + 1:index_selected + s_index]))

# Markov Property Visualization
plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.plot(t, W, label="Path")
plt.plot([t_selected, t_selected + s], [W[index_selected], future_path[-1]], 'ro-', label="Future Path")
plt.title("Markov Property Visualization")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()

# Martingale Property Visualization
plt.subplot(122)
plt.plot(t, W, label="Path")
plt.plot([t_selected, t_selected + s], [W[index_selected], W[index_selected]], 'ro-', label="Conditional Expectation")
plt.title("Martingale Property Visualization")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()

plt.tight_layout()
plt.show()
