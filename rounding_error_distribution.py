import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Definiere den Bereich der x-Werte
x_values = np.arange(-3, 3, 0.000001)
# print(f"x_values: {x_values}")
print(f"len(x_values): {len(x_values)}")

# Berechne die Verteilungsfunktion für jeden x-Wert
y_values = norm.cdf(x_values)
# print(f"y_values: {y_values}")
#
# # Plotte die Verteilungsfunktion
# plt.plot(x_values, y_values, label='Standardnormalverteilung')
#
# # Beschriftungen und Titel hinzufügen
# plt.title('Verteilungsfunktion der Standardnormalverteilung')
# plt.xlabel('x')
# plt.ylabel('Verteilungsfunktion')
# plt.legend()

# Zeige den Plot an
# plt.show()

y_round_3 = np.round(y_values, 3)
y_round_10 = np.round(y_values, 10)
# print(f"y_round_3: {y_round_3}")

error_3_abs = np.abs(y_values - y_round_3)
error_3 = y_values - y_round_3

error_3_10 = y_round_10 - y_values
print(f"min, max: {np.min(error_3)}, {np.max(error_3)}")

# # plot error distribution
# plt.plot(x_values, error_3, label='Standardnormalverteilung')
# plt.show()

# plot histogram of error distribution
plt.hist(error_3, bins=100, color='navy', edgecolor='black', alpha=0.2)
plt.show()

# # draw scatterplot between error and x-values
# plt.scatter(x_values, error_3_10)
# plt.show()

# #################### adjust with bar slider ####################
# bin width
# interval width
# range of x-values
