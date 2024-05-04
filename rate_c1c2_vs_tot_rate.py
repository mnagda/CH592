import numpy as np
import matplotlib.pyplot as plt

# Load data from "average_c1c2_vs_Vc.txt" file
data = np.loadtxt("tot_rate.txt")
data2 = np.loadtxt("sim_drip_rate.txt")
V_values_data = data[:, 0]
c1c2_values_data = data[:, 1]
drip_values_data = data2[:, 1]
# Define constants
K = 390 
c= [0.3832304379994471, 0.346569506261546, 0.35131017476248333, 0.4049067702758998, 0.3839116831582421, 0.4022121579143325]
h = 1.05457182e-34 * 5.034e22
V_values = [5, 10, 15, 20, 25, 30]
#print(233*(np.pi*hbar/k *1e15))
# Define the function f(t)
def f(V,i):
    J = np.sqrt(4*V**2 + K**2)
    return (4*V**2 /(h*J))*1e-15*c[i]

# Calculate the average positive value of f(t) for each V value
f_values = []
i=0
for V in V_values:
        f_values.append(f(V,i))
        i+=1

# Plot both on the same graph
plt.plot(V_values, f_values, label='Dripping rate from formula (1st order)')
#plt.plot(V_values_data, c1c2_values_data, label='Total rate from simulations')
plt.plot(V_values_data, drip_values_data, label='Dripping rate from simulations')
plt.title('Comparison of rates from formula with simulated data')
plt.xlabel('Vc')
plt.ylabel('Rates')
plt.legend()
plt.grid(True)
plt.show()
