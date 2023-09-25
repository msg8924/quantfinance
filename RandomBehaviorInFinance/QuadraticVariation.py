import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1.0  # Time horizon
N = 1000  # Number of time steps
dt = T / N  # Time step

# Generate Brownian motion path
t = np.linspace(0.0, T, N+1)
W = np.cumsum(np.sqrt(dt) * np.random.randn(N))

# Calculate quadratic variation
quad_variation = np.cumsum(np.diff(W)**2)

# Create plots
plt.figure(figsize=(12, 5))
print(t)
print(W)
'''
# Brownian motion path
plt.subplot(121)
plt.plot(t, W)
plt.title("Brownian Motion Path")
plt.xlabel("Time")
plt.ylabel("Value")

# Quadratic variation
plt.subplot(122)
plt.plot(t[1:], quad_variation)
plt.title("Quadratic Variation")
plt.xlabel("Time")
plt.ylabel("Value")

plt.tight_layout()
plt.show()
'''
