import matplotlib.pyplot as plt

# Read the data from the text file
data = []
with open('nzrate.txt', 'r') as file:
    for line in file:
        values = line.split()
        if len(values) == 3:
            vc, transfers, avg_time = map(float, values)
            data.append((vc, transfers, avg_time))

# Calculate the rate
rates = [(vc, transfers / avg_time) for vc, transfers, avg_time in data]

# Unzip the rates for plotting
Vc_values, rate_values = zip(*rates)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(Vc_values, rate_values, marker='o', linestyle='-')
plt.title('Rate vs Vc')
plt.xlabel('Vc values')
plt.ylabel('Rate (% transfers / average time)')
plt.grid(True)
plt.show()
