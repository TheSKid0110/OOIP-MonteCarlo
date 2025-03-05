import numpy as np
import matplotlib.pyplot as plt

# Number of simulations
n = 10000000

# Random sampling for each variable
A = np.random.uniform(500, 1000, n)      # Area in acres
h = np.random.uniform(20, 50, n)         # Thickness in feet
phi = np.random.normal(0.2, 0.05, n)     # Porosity, normal distribution
phi = np.clip(phi, 0, 1)                 # Keep porosity between 0 and 1
Sw = np.random.uniform(0.2, 0.4, n)      # Water saturation
Boi = 1.2                                # Oil formation volume factor (constant)

# Calculate OOIP for each iteration
OOIP = (7758 * A * h * phi * (1 - Sw)) / Boi

# Calculate percentiles and mode
p10 = np.percentile(OOIP, 10)
p50 = np.percentile(OOIP, 50)
p90 = np.percentile(OOIP, 90)

# Create histogram
plt.figure(figsize=(10, 6))
counts, bins, _ = plt.hist(OOIP, bins=50, color='skyblue', edgecolor='black', alpha=0.7, density=True)
plt.title('Monte Carlo Simulation: OOIP Distribution', fontsize=14)
plt.xlabel('OOIP (Stock-Tank Barrels)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)

# Estimate mode from histogram
bin_width = bins[1] - bins[0]
mode_bin_index = np.argmax(counts)
mode_estimate = bins[mode_bin_index] + bin_width / 2

# Add vertical lines for P10, P50, P90, and Mode
plt.axvline(p10, color='red', linestyle='--', label=f'P10: {p10:.2f} STB')
plt.axvline(p50, color='green', linestyle='--', label=f'P50: {p50:.2f} STB')
plt.axvline(p90, color='blue', linestyle='--', label=f'P90: {p90:.2f} STB')
plt.axvline(mode_estimate, color='purple', linestyle='--', label=f'Mode: {mode_estimate:.2f} STB')

# Connect the tops of the histogram bars
bin_centers = (bins[:-1] + bins[1:]) / 2  # Midpoint of each bin
plt.plot(bin_centers, counts, color='black', linestyle='-', linewidth=2, label='Histogram Outline')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True, alpha=0.3)
plt.show()

# Print summary statistics
print(f"Total number of data points: {n}")
print(f"Mean OOIP: {np.mean(OOIP):.2f} STB")
print(f"P10: {p10:.2f} STB")
print(f"P50 (Median): {p50:.2f} STB")
print(f"P90: {p90:.2f} STB")
print(f"Mode (approx): {mode_estimate:.2f} STB")