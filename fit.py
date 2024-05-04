import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Fit function for a damped sinusoidal function with an offset
def damped_sinusoid_with_offset(t, A, tau, offset):
    return A * np.exp(-t/tau) + offset

# Define lower and upper bounds for the parameters
lower_bounds = [0, 0, -1000]
upper_bounds = [10000, 10000000, 1000]

# Iterate over each file
for i in range(5, 31, 5):  # Assuming files are named pop5.out, pop10.out, ..., pop30.out
    filename = f'pop{i}.out'
    data = np.loadtxt(filename)

    # Perform the fit with bounds
    popt, _ = curve_fit(damped_sinusoid_with_offset, data[:,0], data[:,2], p0=[1, 100, 0.1], bounds=(lower_bounds, upper_bounds), maxfev=9000)

    # Extract the fitted parameters
    amplitude, tau, offset = popt

    # Plot the fitted curve along with the data
    fit_curve = damped_sinusoid_with_offset(data[:,0], *popt)

    fig, axes = plt.subplots(1, 1, figsize=(10, 6))
    axes.plot(data[:,0], data[:,2], label="Population Decay")
    axes.plot(data[:,0], fit_curve, label=f"Fitted Damped Sinusoid with Amplitude: {amplitude:.2f}, Tau: {tau:.2f}")
    axes.legend(loc=0)
    axes.set_xlabel('Time')
    axes.set_ylabel('Population')
    axes.set_title(f'Curve Fitting - {filename}')
    plt.show()
    print(1/tau)

