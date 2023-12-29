import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# Set the parameter p
p = 1/6

# Generate values for x (number of trials)
x = np.arange(1, 21)  # You can adjust the range as needed

# Calculate the probability mass function (PMF) for each x
pdf = geom.pmf(x, p)

# Calculate the cumulative distribution function (CDF) for each x
cdf = geom.cdf(x, p)

# Plot the probability density function (PDF)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(x, pdf, color='skyblue', edgecolor='black')
plt.title('Geometric Distribution PDF')
plt.xlabel('Number of Trials')
plt.ylabel('Probability')
plt.grid(True)

# Plot the cumulative distribution function (CDF)
plt.subplot(1, 2, 2)
plt.step(x, cdf, color='orange', where='post')
plt.title('Geometric Distribution CDF')
plt.xlabel('Number of Trials')
plt.ylabel('Cumulative Probability')
plt.grid(True)

plt.tight_layout()
plt.show()
