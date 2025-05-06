import numpy as np
import matplotlib.pyplot as plt

# Define parameters
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector
fm = 5  # Message signal frequency
fc = 50  # Carrier signal frequency

# Generate message signal (sine wave)
message_signal = np.sin(2 * np.pi * fm * t)

# Generate carrier signal (pulse train)
carrier_signal = np.zeros_like(t)
pulse_width = 0.01  # Adjust pulse width as needed
for i in range(len(t)):
    if t[i] % (1/fc) < pulse_width:
        carrier_signal[i] = 1

# Perform PAM
pam_signal = message_signal * carrier_signal

# Plot signals
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, message_signal)
plt.title('Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.title('Carrier Signal (Pulse Train)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, pam_signal)
plt.title('PAM Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()