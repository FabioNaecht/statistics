import numpy as np
import matplotlib.pyplot as plt


# plot the function p - p^2
def plot_function(n: int = 100) -> None:
    x = np.linspace(-0.5, 1.5, 100)
    y = (x - x ** 2) * n
    plt.plot(x, y)
    # include x- and y-axis
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


if __name__ == '__main__':
    plot_function(n=0)
