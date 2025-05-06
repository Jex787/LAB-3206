import numpy as np
import matplotlib.pyplot as plt

# Binary input (you can change this)
data = [1, 0, 1, 1, 0, 0, 1]

# Parameters
bit_duration = 1         # seconds per bit
samples_per_bit = 100    # resolution
total_samples = len(data) * samples_per_bit
t = np.linspace(0, len(data) * bit_duration, total_samples)

# Signal generation
signal = []

for bit in data:
    if bit == 1:
        # First half high, second half zero
        signal.extend([1] * (samples_per_bit // 2))
        signal.extend([0] * (samples_per_bit // 2))
    else:
        # Full bit duration zero
        signal.extend([0] * samples_per_bit)

# Plotting
plt.figure(figsize=(10, 3))
plt.plot(t, signal, linewidth=2, color='green')
plt.title("Unipolar RZ (Return-to-Zero) Signaling")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.xticks(np.arange(0, len(data) + 1, 1))
plt.yticks([0, 1])
plt.show()
