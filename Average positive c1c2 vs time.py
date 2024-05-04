import numpy as np
import matplotlib.pyplot as plt

# Define the filename
filename = "fort.2000"

# Initialize lists to store time and c1c2* values
time_list = []
c1c2_list = []

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
c1c2_array = c1c2_array.reshape(num_trajectories, 50001)

# Initialize list to store averaged positive c1c2* values
average_positive_c1c2 = []

# Loop over each trajectory
for trajectory in c1c2_array:
    # Consider only positive values for the current trajectory
    positive_values = trajectory[trajectory > 0]
    # Take the average of positive values and append to the list
    average_positive_c1c2.append(np.mean(positive_values))

# Calculate the overall average of positive c1c2* values
overall_average_positive_c1c2 = np.mean(average_positive_c1c2)
print("Overall average of positive c1c2* values:", overall_average_positive_c1c2)

