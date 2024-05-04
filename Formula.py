import numpy as np
import matplotlib.pyplot as plt

def function(x, a, b, K, J, h, V):
    term1 = a*b * np.sin((-K+J)*x/h)*(K+J)
    term2 = -a*b * np.sin((K+J)*x/h)*(K-J)
    term3 = - np.sin(K*x/h)*(a**2 * (K + J) + b**2 * (K - J))
    return (term1 + term2 + term3)/(2*V)

def func(x, K, J, h, V):
    return (np.sin(J*x/2/h))*(np.cos((K+J/2)*x/h))#(4*V**2 /(h*J))/2/V * h

# Define parameters
K = 390
h = 1.05457*10**(-34) * 5.03445*10**(22)
V = 30
J = np.sqrt(4*V**2 + K**2)
a = V/J
b = -a
# Generate x values
x_values = np.linspace(0, 10000, 100000)
x_values = x_values*10**(-15)
# Calculate corresponding y values
y1_values = function(x_values, a, b, K, J, h, V)
y2_values = func(x_values, K, J, h, V)
# Plot the function
#plt.plot(x_values, y1_values, label='1')
plt.plot(x_values, y2_values, label='2')
plt.title('Plot of the function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
