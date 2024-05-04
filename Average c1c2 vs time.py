import numpy as np
import matplotlib.pyplot as plt

# Define the filename
filename = "30fort.2000"

# Initialize lists to store time and c1c2* values
time_list = []
c1c2_list = []

h = 1.05457*10**(-34)
V = 30*1.98630e-23
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
num_trajectories = int(len(c1c2_array) / 50001)
print(num_trajectories)
c1c2_array = c1c2_array.reshape(num_trajectories, 50001)

average_positive_c1c2_values = []
for t in range(100):
    c1c2_values = c1c2_array[t]
    positive_c1c2_values = c1c2_values[c1c2_values > 0]
    #print(positive_f_values)
    average_positive_c1c2_values.append(np.mean(positive_c1c2_values))

# Calculate the average over all trajectories
average_c1c2 = np.mean(average_positive_c1c2_values)

## Calculate the overall average of positive c1c2* values
print("Overall average rate: ", average_c1c2*2*V/h *1e-15)