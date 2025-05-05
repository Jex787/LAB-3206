import numpy as np
import matplotlib.pyplot as plt

# User Input
bitstream_input = input("Enter the binary data stream (e.g., 1011001): ")
bitstream = [int(b) for b in bitstream_input if b in '01']

# Parameters
bit_duration = 1
sampling_rate = 100
time = np.linspace(0, len(bitstream), len(bitstream) * sampling_rate)
signal = []

# Encoding: 1 → +1, 0 → -1
for bit in bitstream:
    value = [1 if bit == 1 else -1] * sampling_rate
    signal.extend(value)

# Plotting
plt.figure(figsize=(10, 2))
plt.plot(time, signal, linewidth=2)
plt.title("Polar NRZ Line Coding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.show()
