import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the Fourier series function
def fourier_series(t, *coefficients):
    result = coefficients[0]
    for n in range(1, (len(coefficients) - 1) // 2 + 1):
        result += coefficients[2 * n - 1] * np.cos(2 * np.pi * n * t) + coefficients[2 * n] * np.sin(2 * np.pi * n * t)
    return result

# Sample data (replace this with your 2D trajectory data)
t = np.linspace(0, 10, 100)
x_data = 2 * np.cos(2 * np.pi * 1 * t) + 1 * np.sin(2 * np.pi * 2 * t) + np.random.normal(scale=0.1, size=len(t))
y_data = 1 * np.cos(2 * np.pi * 1 * t) + 0.5 * np.sin(2 * np.pi * 2 * t) + np.random.normal(scale=0.1, size=len(t))

# Fit the X data using curve_fit
num_terms = 5  # Adjust the number of terms as needed
initial_guess = [1.0] * (2 * num_terms + 1)
fit_coefficients_x, _ = curve_fit(fourier_series, t, x_data, p0=initial_guess)

# Fit the Y data using curve_fit
fit_coefficients_y, _ = curve_fit(fourier_series, t, y_data, p0=initial_guess)

# Generate the fitted curves
fitted_curve_x = fourier_series(t, *fit_coefficients_x)
fitted_curve_y = fourier_series(t, *fit_coefficients_y)

# Plot the original data and the fitted curves
plt.plot(t, x_data, 'o', label='Original X Data')
plt.plot(t, y_data, 'o', label='Original Y Data')
plt.plot(t, fitted_curve_x, label='Fitted X Curve')
plt.plot(t, fitted_curve_y, label='Fitted Y Curve')
plt.legend()
plt.show()
