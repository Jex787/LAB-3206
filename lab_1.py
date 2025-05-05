import numpy as np
import matplotlib.pyplot as plt

# User Input
bitstream_input = input("Enter the binary data stream (e.g., 1011001): ")
bitstream = [int(b) for b in bitstream_input if b in '01']

# Signal generation
bit_duration = 1
sampling_rate = 100
time = np.linspace(0, len(bitstream), len(bitstream) * sampling_rate)
signal = []

for bit in bitstream:
    value = [bit] * sampling_rate  # 1 for '1', 0 for '0'
    signal.extend(value)

# Plotting
plt.figure(figsize=(10, 2))
plt.plot(time, signal, linewidth=2)
plt.title("Unipolar NRZ Line Coding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.show()
