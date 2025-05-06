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
# Lab-01(unipolar NRZ)
# for bit in data:
#     if bit == 1:
#         signal.extend([1] * samples_per_bit)
#     else:
#         signal.extend([0] * samples_per_bit)


# unipolar RZ
# for bit in data:
#     if bit == 1:
#         # First half high, second half zero
#         signal.extend([1] * (samples_per_bit // 2))
#         signal.extend([0] * (samples_per_bit // 2))
#     else:
#         # Full bit duration zero
#         signal.extend([0] * samples_per_bit)


# Polar_NRZ
# signal = np.zeros(len(t))
# for i, bit in enumerate(data):
#     start = i * samples_per_bit
#     end = start + samples_per_bit
#     if bit == 1:
#         signal[start:end] = 1
#     else:
#         signal[start:end] = -1

# Bio-polar NRZ

# signal = np.zeros(len(t))
# polarity = 1  # Start with positive voltage for first '1'
# for i, bit in enumerate(data):
#     start = i * samples_per_bit
#     mid = start + samples_per_bit // 2
#     if bit == 1:
#         signal[start:mid] = polarity
#         polarity *= -1

# split-phase(Manchester)

# signal = np.zeros(len(t))
# for i, bit in enumerate(data):
#     start = i * samples_per_bit
#     mid = start + samples_per_bit // 2
#     end = start + samples_per_bit
#     if bit == 1:
#         # For '1': High-to-Low transition
#         signal[start:mid] = 1
#         signal[mid:end] = -1
#     else:
#         # For '0': Low-to-High transition
#         signal[start:mid] = -1
#         signal[mid:end] = 1


# Plotting
plt.figure(figsize=(10, 3))
plt.plot(t, signal, linewidth=2, color='blue')
plt.title("Line coding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.show()
