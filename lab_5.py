import numpy as np
import matplotlib.pyplot as plt

# Input binary data
data = input("Enter binary sequence (e.g., 1011001): ")
data = [int(bit) for bit in data]

# Parameters
bit_duration = 1
samples_per_bit = 100
t = np.linspace(0, bit_duration * len(data), len(data) * samples_per_bit)
signal = []

# Manchester Encoding
# 1 → High to Low: [1, -1]
# 0 → Low to High: [-1, 1]

for bit in data:
    if bit == 1:
        first_half = [1] * (samples_per_bit // 2)
        second_half = [-1] * (samples_per_bit // 2)
    else:
        first_half = [-1] * (samples_per_bit // 2)
        second_half = [1] * (samples_per_bit // 2)
    signal.extend(first_half + second_half)

# Plotting
plt.figure(figsize=(10, 3))
plt.plot(t, signal, drawstyle='steps-post', linewidth=2)
plt.title("Manchester (Split-Phase) Line Coding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.show()
