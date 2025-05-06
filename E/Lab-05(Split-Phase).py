import numpy as np
import matplotlib.pyplot as plt

# Input binary data
data = [1, 0, 1, 1, 0, 0, 1]
bit_duration = 1       # Duration of one bit (in seconds)
samples_per_bit = 100  # Number of samples per bit

# Time vector for entire signal
t = np.linspace(0, bit_duration * len(data), samples_per_bit * len(data))

# Generate Manchester encoded signal
signal = np.zeros(len(t))
for i, bit in enumerate(data):
    start = i * samples_per_bit
    mid = start + samples_per_bit // 2
    end = start + samples_per_bit
    if bit == 1:
        # For '1': High-to-Low transition
        signal[start:mid] = 1
        signal[mid:end] = -1
    else:
        # For '0': Low-to-High transition
        signal[start:mid] = -1
        signal[mid:end] = 1

# Plotting the Manchester waveform
plt.figure(figsize=(10, 3))
plt.plot(t, signal, linewidth=2)
plt.title("Split-Phase (Manchester) Signaling")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim([-1.5, 1.5])
plt.grid(True)
plt.xticks(np.arange(0, len(data) + 1, 1))
plt.yticks([-1, 0, 1])
plt.show()
