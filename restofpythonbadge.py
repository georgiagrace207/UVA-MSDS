# NOTE: At this time, I cannot get matplotlib to work. I am currently working on troubleshooting. In the meantime, I
# will attempt to write programs that would answer the badge questions had matplot been working.

# QUESTION 4:

# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate samples

sample_count = 1000

n_val = 20
p_val = 0.5
b_samples = np.random.binomial(n_val, p_val, sample_count)

low = 0
high = 10
u_samples = np.random.uniform(low, high, sample_count)

mean = 0
std_dev = 1
n_samples = np.random.normal(mean, std_dev, sample_count)

# Creating histograms

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(b_samples, bins=20, color='red', alpha=0.7)
plt.title('Histogram of Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(u_samples, bins=20, color='cyan', alpha=0.7)
plt.title('Histogram of Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(n_samples, bins=20, color='yellow', alpha=0.7)
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# QUESTION 5

# Setting parameters:

p = 0.5
sample_size = 1000
trials = [10, 50, 100, 500]

# Generating samples

b_samples = {}
for j in trials:
    b_samples[j] = np.random.binomial(j, p, sample_size)

mean_n = p * np.array(trials)
std_dev_n = np.sqrt(p * (1 - p) * np.array(trials))
n_samples = np.random.normal(mean_n, std_dev_n, (sample_size, len(trials)))

# Creating histograms

plt.figure(figsize=(12, 8))

for i, j in enumerate(trials):
    plt.subplot(2, 2, i + 1)
    plt.hist(b_samples[j], bins=20, density=True, alpha=0.6, color='blue', label=f'Binomial (N={j})')

    # Plot the corresponding Normal distribution
    plt.hist(n_samples[:, i], bins=20, density=True, alpha=0.6, color='red', label='Normal')

    plt.title(f'N = {j}')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()

plt.tight_layout()
plt.show()

# Question 6

file = "C:/Users/Georgia Davidson/Downloads/MSDS-Orientation-Computer-Survey.xlsx"
df = pd.read_csv(file)

ram_column = df['RAM (in GB)']
plt.figure(figsize=(10, 6))
plt.hist(ram_column, bins=20, color='purple', alpha=0.7)
plt.title('RAM Distribution among MSDS students')
plt.xlabel('RAM (GB)')
plt.ylabel('Frequency')

plt.grid(True)
plt.show()

ram_column = df['CPU Cycle Rate (in GHz)']
plt.figure(figsize=(10, 6))
plt.hist(ram_column, bins=20, color='green', alpha=0.7)
plt.title('CPU Cycle Rate among MSDS students')
plt.xlabel('Rate')
plt.ylabel('Frequency')

plt.grid(True)
plt.show()

ram_column = df['CPU Number of Cores (int)']
plt.figure(figsize=(10, 6))
plt.hist(ram_column, bins=20, color='blue', alpha=0.7)
plt.title('Cores Number among MSDS students')
plt.xlabel('Cores')
plt.ylabel('Frequency')

plt.grid(True)
plt.show()

# Qualitative descriptions:

# Students had a mix of MacOS, Windows, and Linux operating systems.

# Hard drives ranged from 16 to over 4000.

# CUDA cores ranged from 0 to over 6000.

# There were a broad range of GPU strings students had.
















