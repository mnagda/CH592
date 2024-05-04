import numpy as np
import matplotlib.pyplot as plt

# Load data from "average_c1c2_vs_Vc.txt" file
data = np.loadtxt("50_average_positive_c1c2_vs_Vc.txt")
V_values_data = data[:, 0]
c1c2_values_data = data[:, 1]

# Define constants
K = 410 
h = 1.05457182e-34 * 5.034e22
V_values = [5, 10, 15, 20, 25, 30]
#print(233*(np.pi*hbar/k *1e15))
# Define the function f(t)
def function(x, K, h, V):
    K = 390
    h = 1.05457*10**(-34) * 5.03445*10**(22)
    J = np.sqrt(4*V**2 + K**2)
    a = V/J
    b = -a
    term1 = a*b * np.sin((-K+J)*x/h)*(K+J)
    term2 = -a*b * np.sin((K+J)*x/h)*(K-J)
    term3 = - np.sin(K*x/h)*(a**2 * (K + J) + b**2 * (K - J))
    return (np.sin(J*x/2/h))*(np.cos((K+J/2)*x/h))*(4*V**2 /(h*J))

# Generate a range of t values from 0 to 10000
t_values = np.arange(0, 10001) * 1e-15

# Calculate the average positive value of f(t) for each V value
average_positive_f_values = []
for V in V_values:
    f_values = function(t_values, K, h, V)
    positive_f_values = f_values[f_values > 0]
    average_positive_f = np.mean(positive_f_values)
    average_positive_f_values.append(average_positive_f)

# Plot both on the same graph
plt.loglog(V_values, average_positive_f_values, label='Average positive log(Img[c1c2*]) from formula (1st order)')
plt.loglog(V_values_data, c1c2_values_data, label='Average positive log(Img[c1c2*]) from simulations')
plt.title('Comparison of log(Img[c1c2*]) from formula with simulated data for Lambda = 90')
plt.xlabel('log(Vc)')
plt.ylabel('log(Img[c1c2*])')
plt.legend()
plt.grid(True)
plt.show()
