import numpy as np
import matplotlib.pyplot as plt

# User input for binary data
data_str = input("Enter binary data (e.g., 1010101): ")
x = [int(bit) for bit in data_str if bit in '01']

# Parameters
bp = 1e-6
A1, A2 = 10, 5
f = (1 / bp) * 10
samples = 100
t_bit = np.linspace(0, bp, samples)
t_total = np.linspace(0, bp * len(x), len(x) * samples)

# Digital signal
digital_signal = np.repeat(x, samples)

# Modulation
modulated = np.concatenate([
    (A1 if bit else A2) * np.cos(2 * np.pi * f * t_bit)
    for bit in x 
])

# Demodulation
carrier = np.cos(2 * np.pi * f * t_bit)
recovered = [
    1 if (2 * np.trapz(modulated[i:i+samples] * carrier, t_bit) / bp) > 7.5 else 0
    for i in range(0, len(modulated), samples)
]
received_signal = np.repeat(recovered, samples)

# Plotting
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t_total, digital_signal, lw=2.5)
plt.title("Transmitting Information as Digital Signal")
plt.ylabel("Amplitude"); plt.grid(True); plt.ylim(-0.5, 1.5)

plt.subplot(3, 1, 2)
plt.plot(t_total, modulated)
plt.title("Waveform for Binary ASK Modulation")
plt.ylabel("Amplitude"); plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_total, received_signal, lw=2.5)
plt.title("Received Information as Digital Signal")
plt.xlabel("Time (sec)"); plt.ylabel("Amplitude"); plt.grid(True); plt.ylim(-0.5, 1.5)

plt.tight_layout()
plt.show()

# Print results
print("Transmitted Data: ", x)
print("Received Data:    ", recovered)
