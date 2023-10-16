import numpy as np
import matplotlib.pyplot as plt

# Option parameters
strike_price = 100  # Strike price (K)
premium = 5         # Premium paid for the call (C)

# Range of final prices for the underlying asset (S_T)
final_prices = np.linspace(80, 120, 100)

# Calculate the value of the long call option at expiration
option_values = np.maximum(0, final_prices - strike_price) - premium

# Calculate the option's payout at expiration
option_payout = np.maximum(0, final_prices - strike_price)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the option value
plt.plot(final_prices, option_values, label='Long Call Option Value')

# Plot the option's payout
plt.plot(final_prices, option_payout, label='Long Call Option Payout', linestyle='--')

# Add labels and title
plt.xlabel('Final Price of Underlying Asset (S_T)')
plt.ylabel('Option Value / Payout')
plt.title('Long Call Option Value and Payout vs. Final Asset Price')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
