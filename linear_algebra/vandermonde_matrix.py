import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


coordinates = np.array([[0, 1], [2/3, 1/2], [1, 0], [1.5, -0.5], [2, 0.2], [2.5, 3]])
x_coordinates = coordinates[:, 0]
y_coordinates = coordinates[:, 1]
vandermond_matrix = np.vander(x_coordinates, increasing=True)
print(f"Vandermond matrix:\n{vandermond_matrix}\n")

# solve the system of linear equations
coefficients = np.linalg.solve(vandermond_matrix, y_coordinates)
print(f"coefficients:\n{coefficients}\n")

# determine polynomial function from coefficients with lamda
polynomial_function = lambda x: coefficients[-1] * x ** 5 + coefficients[-2] * x ** 4 + coefficients[-3] * x ** 3 + \
                                    coefficients[-4] * x ** 2 + coefficients[-5] * x + coefficients[-6]

# determine a spline function from the coordinates
spline_function = CubicSpline(x_coordinates, y_coordinates)

# determine bezier curve fit
# bezier_curve = bezier.Curve(coordinates, degree=5)


# plot coordinates and polynomial fit
x = np.linspace(min(x_coordinates), max(y_coordinates), 100)
plt.plot(x_coordinates, y_coordinates, 'o')
# plot the polynomial function
plt.plot(x, polynomial_function(x))
# plot the spline function
plt.plot(x, spline_function(x), '--')
plt.title('Trajectory Fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['data', 'Vandermonde matrix fit', 'cubic spline fit'])

plt.show()
