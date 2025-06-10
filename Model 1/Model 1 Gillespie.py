import numpy as np
import matplotlib.pyplot as plt

# Parameters
pi = 0.7          # Rate of monomer addition
epsilon = 0.4     # Rate of monomer removal
T = 1000           # Total simulation time
num_paths = 1000  # Number of sample paths


# Storage for results
final_lengths = []

for i in range(num_paths):
    t = 0.0
    n = 10  # Initial polymer length
    while t < T and n >= 0:

        total_rate = pi + epsilon

        # Time to next reaction (exponential distribution)
        dt = np.random.exponential(1.0 / total_rate)
        t += dt
        if t >= T:
            break

        # Decide which reaction occurs
        if np.random.rand() < pi / total_rate:
            n += 1  # Add monomer
        else:
            n = max(0, n - 1)  # Remove monomer, but don't go below 0

    final_lengths.append(n)

max_n = max(final_lengths)
hist_bins = np.arange(0, max_n + 2)

plt.figure(figsize=(8, 5))
plt.hist(final_lengths, bins=hist_bins, density=True, align='left', color='skyblue', edgecolor='black')
plt.xlabel('Polymer length n')
plt.ylabel('Probability $P_n(T)$')
plt.title(f'Distribution of $P_n(T)$ at $T = {num_paths}$ (Gillespie)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
