import numpy as np
import matplotlib.pyplot as plt

# Define constants
K = 250 
h = 1.05457182e-34 * 5.034e22
V_values = np.linspace(5,30,1000)
#print(233*(np.pi*hbar/k *1e15))
# Define the function f(t)
def f(x, V):
    J = np.sqrt(4*V**2 + K**2)
    return (np.sin(J*x/2/h))*(np.cos((K+J/2)*x/h))#*(4*V**2 /(h*J))/2/V * h

# Generate a range of t values from 0 to 10000
t_values = np.arange(0, 100001) * 1e-15

# Calculate the average positive value of f(t) for each V value
average_positive_f_values = []
for V in V_values:
    f_values = f(t_values, V)
    positive_f_values = f_values[f_values > 0]
    average_positive_f = np.mean(positive_f_values)
    average_positive_f_values.append(average_positive_f)

# Plot the average positive value of f(t) against V
plt.plot(V_values, average_positive_f_values)
plt.title('Average positive f(t) vs V')
plt.xlabel('V')
plt.ylabel('Average positive f(t)')
plt.grid(True)
plt.show()
