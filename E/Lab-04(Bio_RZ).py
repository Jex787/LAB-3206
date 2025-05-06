import numpy as np
import matplotlib.pyplot as plt

# Input binary data
data = [1, 0, 1, 1, 0, 0, 1]
bit_duration = 1  # Assume 1 second for simplicity
samples_per_bit = 100
t = np.linspace(0, bit_duration * len(data), samples_per_bit * len(data))

# Generate bipolar RZ signal
signal = np.zeros(len(t))
polarity = 1  # Start with positive voltage for first '1'
for i, bit in enumerate(data):
    start = i * samples_per_bit
    mid = start + samples_per_bit // 2
    if bit == 1:
        signal[start:mid] = polarity
        polarity *= -1  # Alternate polarity for next 1

# Plot the waveform
plt.figure(figsize=(10, 3))
plt.plot(t, signal, linewidth=2)
plt.title("Bipolar RZ Signaling")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim([-1.5, 1.5])
plt.grid(True)
plt.xticks(np.arange(0, len(data)+1, 1))
plt.yticks([-1, 0, 1])
plt.show()
