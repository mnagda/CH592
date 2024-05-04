import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt("average_c1c2_vs_Vc.txt")

# Extract columns
first_column = data[:, 0]
second_column = data[:, 1]

# Plot the second column against the first column
plt.plot(first_column, second_column)
plt.title('Plot of Second Column vs. First Column')
plt.xlabel('First Column')
plt.ylabel('Second Column')
plt.grid(True)
plt.show()
