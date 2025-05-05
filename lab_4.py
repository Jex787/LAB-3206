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

# Start polarity
last_polarity = -1

for bit in data:
    if bit == 1:
        last_polarity *= -1
        half_bit = [last_polarity] * (samples_per_bit // 2)
        other_half = [0] * (samples_per_bit - len(half_bit))
        signal.extend(half_bit + other_half)
    else:
        signal.extend([0] * samples_per_bit)

# Plotting
plt.figure(figsize=(10, 3))
plt.plot(t, signal, drawstyle='steps-post', linewidth=2)
plt.title('Bi-polar Return to Zero (RZ) Line Coding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.show()
