import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data=np.loadtxt('average_c1c2_vs_Vc.txt')

#plt.plot(data[:,0],data[:,1],label='c1')
#plt.plot(data[:,0],data[:,2],label='c2')
#plt.title("Population")
#plt.xlabel("x")
#plt.legend()
#plt.ylabel("$c_i$")
#plt.tight_layout()
#plt.savefig("half_CC_c1.png")
#plt.show()

# Fit function for a damped sinusoidal function with an offset
def damped_sinusoid_with_offset(x, A, C):
    return A * x + C

# Define lower and upper bounds for the parameters
lower_bounds = [-1000, -1000, -1000]
upper_bounds = [1000, 1000, 1000]

# Perform the fit with bounds
popt, _ = curve_fit(damped_sinusoid_with_offset, np.log(data[:,0]), np.log(data[:,1]), p0=[1, 0.1], maxfev=9000)

# Extract the fitted parameters
A, C = popt

# Plot the fitted curve along with the data
fit_curve = damped_sinusoid_with_offset(np.log(data[:,0]), *popt)

#print(f"Rate constant (k): {rate_const}")

fig, axes = plt.subplots(1, 1, figsize=(10, 6))
axes.plot(np.log(data[:,0]), np.log(data[:,1]), label="log(Im[c1c2*])")
axes.plot(np.log(data[:,0]), fit_curve, label=f"Fitted log line with A: {A}, C: {C}")
axes.legend(loc=0)
axes.set_xlabel('log(V12)')
axes.set_ylabel('log(Im[c1c2*])')
axes.set_title('Curve Fitting')
plt.show()
