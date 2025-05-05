import numpy as np
import matplotlib.pyplot as plt

# User input
data_str = input("Enter binary data (e.g., 1100101): ")
x = [int(bit) for bit in data_str if bit in '01']

# Parameters
bp = 1e-6
A = 5
fc = 2 / bp
samples = 100
t_bit = np.linspace(0, bp, samples, endpoint=False)
t_total = np.linspace(0, bp * len(x), len(x) * samples, endpoint=False)

# Digital signal for plotting
digital_signal = np.repeat(x, samples)

# BPSK Modulation
modulated = np.concatenate([
    A * np.cos(2 * np.pi * fc * t_bit) if bit == 1 else
    -A * np.cos(2 * np.pi * fc * t_bit) for bit in x
])

# Coherent Demodulation
recovered = []
for i in range(0, len(modulated), samples):
    segment = modulated[i:i+samples]
    ref = A * np.cos(2 * np.pi * fc * t_bit)
    product = segment * ref
    integral = np.trapz(product, t_bit)
    recovered.append(1 if integral > 0 else 0)

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
plt.title("Waveform for Binary PSK Modulation")
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
