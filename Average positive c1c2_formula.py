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
    #return (4*V**2 /(h*J))*(np.sin(J*x/2/h))*(np.cos((K+J/2)*x/h))/2/V * h
    return (np.sin(J*x/2/h))*(np.cos((K+J/2)*x/h))*(4*V**2 /(h*J))

# Generate a range of t values from 0 to 10000
t_values = np.arange(0, 100000) * 1e-15

# Calculate the average positive value of f(t) for each V value
average_positive_f_values = []
average_negative_f_values = []
for V in V_values:
    f_values = f(t_values, V)
    positive_f_values = f_values[f_values > 0]
    negative_f_values = f_values[f_values < 0]
    average_positive_f = np.mean(positive_f_values)
    average_positive_f_values.append(average_positive_f)
    average_negative_f = np.mean(negative_f_values)
    average_negative_f_values.append(average_negative_f)

diff = np.zeros(len(V_values))
for i in range(len(V_values)):
    diff[i] = average_positive_f_values[i] + average_negative_f_values[i]

# Plot the average positive value of f(t) against V
plt.plot(V_values, average_positive_f_values, label='average_positive_f_values')
#plt.plot(V_values, average_negative_f_values, label='average_negative_f_values')
#plt.plot(V_values, diff, label='difference')
plt.title('Difference in average f(t) vs V')
plt.xlabel('V')
plt.ylabel('Difference in f(t)')
plt.grid(True)
plt.show()
print(average_positive_f_values)