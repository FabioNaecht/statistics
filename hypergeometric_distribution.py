import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Parameters
# N = 45  # Population size
# n = 6   # Number of draws
# K = 6  # Number of success states in the population

N, K, n = 45, 6, 6

# Define the hypergeometric distribution
rv = hypergeom(N, K, n)

# Calculate the probabilities for each possible outcome
x = np.arange(0, n + 1)
pmf = rv.pmf(x)
cdf = rv.cdf(x)  # Calculate the cumulative distribution function (CDF)

# Create a subplot with two plots side by side
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

# Plot the probability mass function (PMF)
axs[0].bar(x, pmf, align='center', alpha=0.5)
axs[0].set_xticks(x)
axs[0].set_xlabel("Number of Successes")
axs[0].set_ylabel("Probability")
axs[0].set_title("Hypergeometric PMF")
# # log scale
# axs[0].set_yscale('log')

# Plot the cumulative distribution function (CDF)
axs[1].step(x, cdf, where='mid')
axs[1].set_xticks(x)
axs[1].set_xlabel("Number of Successes")
axs[1].set_ylabel("Cumulative Probability")
axs[1].set_title("Hypergeometric CDF")

plt.tight_layout()
plt.show()

