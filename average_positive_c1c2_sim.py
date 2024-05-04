import numpy as np
import matplotlib.pyplot as plt

# Define the filename
filename = "30fort.2000"

# Initialize lists to store time and c1c2* values
time_list = []
c1c2_list = []

h = 1.05457 * 10**(-34)
V = 30 * 1.98630e-23

# Read data from the file
with open(filename, 'r') as file:
    for line in file:
        # Split the line into time and c1c2* values
        time, c1c2 = map(float, line.split())
        time_list.append(time)
        c1c2_list.append(c1c2)

# Convert lists to numpy arrays for easier manipulation
time_array = np.array(time_list)
c1c2_array = np.array(c1c2_list)

# Reshape the c1c2_array to have the same number of rows as trajectories
num_trajectories = int(len(c1c2_array) / 100001)
c1c2_array = c1c2_array.reshape(num_trajectories, 100001)

# Filter out positive values
positive_values = c1c2_array[c1c2_array > 0]

# Calculate the average over all positive values
average_positive = np.mean(positive_values)

# Plot the histogram of positive values
plt.hist(positive_values, bins=50, density=True, alpha=0.6, color='g', label='Positive Values')
plt.axvline(average_positive, color='k', linestyle='dashed', linewidth=1, label=f'Average Positive Value: {average_positive:.4f}')
plt.title('Histogram of Positive c1c2* Values')
plt.xlabel('c1c2*')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the overall average of positive c1c2* values
if h != 0:
    overall_average_positive = average_positive * 2 * V / h * 1e-15
    print("Overall average of positive c1c2* values:", overall_average_positive)
else:
    print("Error: Division by zero due to 'h' being zero.")
