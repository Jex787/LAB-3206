import numpy as np
import matplotlib.pyplot as plt

# Binary input (you can change this)
data = [1, 0, 1, 1, 0, 0, 1]

# Duration setup
bit_duration = 1     # 1 second per bit (for simplicity)
samples_per_bit = 100  # Resolution (samples per bit)
total_samples = len(data) * samples_per_bit

# Time axis
t = np.linspace(0, len(data) * bit_duration, total_samples)

# Signal generation
signal = []

for bit in data:
    if bit == 1:
        signal.extend([1] * samples_per_bit)
    else:
        signal.extend([0] * samples_per_bit)

# Plotting
plt.figure(figsize=(10, 3))
plt.plot(t, signal, linewidth=2, color='blue')
plt.title("Unipolar NRZ Signaling")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-1.5, 1.5)
plt.grid(True)
# plt.xticks(np.arange(0, len(data) + 1, 1))
# plt.yticks([0, 1])
plt.show()
