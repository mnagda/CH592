import matplotlib.pyplot as plt

# Read data from the first file
data1 = {}
with open('./Drip_V/sim_drip_rate.txt', 'r') as file:
    for line in file:
        values = line.split()
        if len(values) == 2:
            key = float(values[0])
            value = float(values[1])
            data1[key] = value

# Read data from the second file
data2 = {}
with open('./500Drip_V/sim_drip_rate.txt', 'r') as file:
    for line in file:
        values = line.split()
        if len(values) == 2:
            key = float(values[0])
            value = float(values[1])
            data2[key] = value

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(list(data1.keys()), list(data1.values()), label='Hop')
plt.plot(list(data2.keys()), list(data2.values()), label='No Hop')
plt.title('Comparison of Data')
plt.xlabel('V12')
plt.ylabel('Rates')
plt.legend()
plt.grid(True)
plt.show()

