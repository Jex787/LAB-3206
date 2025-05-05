import numpy as np
import matplotlib.pyplot as plt

# User input for binary data
data_str = input("Enter binary data (e.g., 1011001): ")
x = [int(bit) for bit in data_str if bit in '01']

# Parameters
bp = 1e-6   # Bit period
A = 5       # Amplitude
f1 = 10 / bp   # Frequency for bit 1
f2 = 5 / bp    # Frequency for bit 0
samples = 100
t_bit = np.linspace(0, bp, samples, endpoint=False)
t_total = np.linspace(0, bp * len(x), len(x) * samples, endpoint=False)

# Digital signal generation
digital_signal = np.repeat(x, samples)

# FSK Modulation
modulated = np.concatenate([
    A * np.cos(2 * np.pi * (f1 if bit else f2) * t_bit) for bit in x
])

# Coherent Demodulation
recovered = []
for i in range(0, len(modulated), samples):
    segment = modulated[i:i+samples]
    corr1 = np.trapz(segment * np.cos(2 * np.pi * f1 * t_bit), t_bit)
    corr2 = np.trapz(segment * np.cos(2 * np.pi * f2 * t_bit), t_bit)
    recovered.append(1 if corr1 > corr2 else 0)

received_signal = np.repeat(recovered, samples)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_total, digital_signal, lw=2.5)
plt.title("Transmitting Information as Digital Signal")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-0.5, 1.5)

plt.subplot(3, 1, 2)
plt.plot(t_total, modulated)
plt.title("Waveform for Binary FSK Modulation")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_total, received_signal, lw=2.5)
plt.title("Received Information as Digital Signal")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-0.5, 1.5)

plt.tight_layout()
plt.show()

# Display data
print("Transmitted Data: ", x)
print("Received Data:    ", recovered)
