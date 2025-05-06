import numpy as np
import matplotlib.pyplot as plt

bitstream_input = input("Enter the binary data: ")
bitstream = [int(b) for b in bitstream_input if b in '01']

bit_duration = 1
sampling_rate = 100
time = np.linspace(0, len(bitstream), len(bitstream) * sampling_rate)
signal = []

# uni-pol NRZ
# -------------------------------------------------
# for bit in bitstream:
#     value = [bit] * sampling_rate
#     signal.extend(value)
# -------------------------------------------------

# Polar NRZ
# -------------------------------------------------
# for bit in bitstream:
#     value = [1 if bit == 1 else -1] * sampling_rate
#     signal.extend(value)
# --------------------------------------------------

# uni-pol RZ
# -------------------------------------------------
# for bit in bitstream:
#     if bit == 1:
#         first_half = [1] * (sampling_rate // 2)
#         second_half = [0] * (sampling_rate - len(first_half))
#         signal.extend(first_half + second_half)
#     else:
#         signal.extend([0] * sampling_rate)
# -------------------------------------------------

# bi-polar RZ
# ------------------------------------------------
# last_polarity = -1
# for bit in bitstream:
#     if bit == 1:
#         last_polarity *= -1
#         first_half = [last_polarity] * (sampling_rate // 2)
#         second_half = [0] * (sampling_rate - len(first_half))
#         signal.extend(first_half + second_half)
#     else:
#         signal.extend([0] * sampling_rate)
# ------------------------------------------------

# Manchester(split phase)
# -----------------------------------------------
# for bit in bitstream:
#     if bit == 1:
#         first_half = [1] * (sampling_rate // 2)
#         second_half = [-1] * (sampling_rate - len(first_half))
#     else:
#         first_half = [-1] * (sampling_rate // 2)
#         second_half = [1] * (sampling_rate - len(first_half))
#     signal.extend(first_half + second_half)
# -----------------------------------------------

plt.figure(figsize=(11,3))

plt.plot(time, signal, linewidth = 3)
plt.title("test(1-5)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-1.5, 1.5)

plt.grid(True)
plt.show()
