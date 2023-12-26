import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons


# Initial parameters
range_x = 6
interval_x = 0.01
bin_nr = 20

# Specify x-values
x_values = np.arange(-range_x/2, range_x/2, interval_x)

# Compute cdf and round to 3 decimal places
y_values = norm.cdf(x_values)
y_round_3 = np.round(y_values, 3)

# Compute error
error_3 = y_values - y_round_3

# Create figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

# Initial plot of error histogram
hist, bins, _ = ax.hist(error_3, bins=bin_nr, color='navy', edgecolor='black', alpha=0.2)

# Specify sliders
ax_bin_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_range_slider = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_interval_slider = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_radio_scaling = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor='lightgoldenrodyellow')

slider_bin = Slider(ax_bin_slider, label='Bin Number', valmin=1, valmax=200, valinit=bin_nr, valstep=1)
slider_range = Slider(ax_range_slider, label='X Range', valmin=4, valmax=20, valinit=range_x, valstep=0.1)
slider_interval = Slider(ax_interval_slider, label='X Interval', valmin=0.00001, valmax=0.01, valinit=interval_x, valstep=0.00001)
radio = RadioButtons(ax_radio_scaling, ('linear', 'log'))


def log_bool_fun(label) -> bool:
    """Adjust scaling of y-axis"""
    # TODO RadioButtons do not adjust immediately after clicking
    log_bool = False

    if label == 'linear':
        log_bool = False
    if label == 'log':
        log_bool = True
    fig.canvas.draw_idle()

    return log_bool


def update(val) -> None:
    """Update function for sliders"""
    # global range_x, interval_x, bin_nr

    # Update parameters from sliders
    bin_nr = int(slider_bin.val)
    range_x = slider_range.val
    interval_x = slider_interval.val

    # Update x-values
    x_values = np.arange(-range_x / 2, range_x / 2, interval_x)

    # Compute cdf and round to 3 decimal places
    y_values = norm.cdf(x_values)
    y_round_3 = np.round(y_values, 3)

    # Compute error
    error_3 = y_values - y_round_3
    # Update histogram
    ax.clear()

    log_bool = log_bool_fun(radio.value_selected)
    hist, bins, _ = ax.hist(error_3, bins=bin_nr, color='navy', edgecolor='black', alpha=0.2, log=log_bool)

    # title
    max_abs_error = np.max(np.abs(error_3))
    mean_abs_error = np.mean(np.abs(error_3))
    title = f'max abs error: {max_abs_error:.4f}\nmean abs error: {mean_abs_error:.5f}'
    ax.set_title(title)

    plt.draw()


# Attach update function to sliders
slider_bin.on_changed(update)
slider_range.on_changed(update)
slider_interval.on_changed(update)

# Attach update function to radio buttons
radio.on_clicked(log_bool_fun)

plt.show()
