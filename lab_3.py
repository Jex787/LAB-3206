import numpy as np
import matplotlib.pyplot as plt

# User input
bitstream_input = input("Enter the binary data stream (e.g., 1011001): ")
bitstream = [int(b) for b in bitstream_input if b in '01']

# Parameters
bit_duration = 1
sampling_rate = 100
samples_per_bit = sampling_rate
time = np.linspace(0, len(bitstream), len(bitstream) * samples_per_bit)

# Encoding
signal = []
for bit in bitstream:
    if bit == 1:
        high = [1] * (samples_per_bit // 2)
        low = [0] * (samples_per_bit // 2)
        signal.extend(high + low)
    else:
        signal.extend([0] * samples_per_bit)

# Plotting
plt.figure(figsize=(10, 2))
plt.plot(time, signal, linewidth=2)
plt.title("Uni-polar RZ Line Coding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.show()
