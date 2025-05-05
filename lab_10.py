import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# User input
fc = int(input("Enter carrier frequency (Hz), e.g., 20: "))
fm = int(input("Enter message frequency (Hz), e.g., 2: "))
fs = int(input("Enter sampling frequency (Hz), e.g., 1000: "))
duration = float(input("Enter signal duration (seconds), e.g., 1: "))
duty = int(input("Enter duty cycle of pulse (%), e.g., 20: "))

# Time axis
t = np.arange(0, duration, 1/fs)

# Message signal (with delay like MATLAB's (n-1))
m = np.sin(2 * np.pi * fm * (t - 1/fs))

# Pulse train (square wave with correct duty cycle fraction)
pulse_train = square(2 * np.pi * fc * t, duty / 100)
pulse_train[pulse_train < 0] = 0  # Make it 0 or 1

# PAM signal
pam = np.zeros_like(t)
period_samples = int(len(t) / fc)
on_samples = int(np.ceil(period_samples * duty / 100))
indices = np.arange(0, len(t), period_samples)

for i in indices:
    pam[i:i+on_samples] = m[i]

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3,1,1)
plt.plot(t, pulse_train)
plt.title('Pulse Train')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.ylim([-0.2, 1.2])
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, m)
plt.title('Message Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.ylim([-1.2, 1.2])
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, pam)
plt.title('PAM Signal (Sample-and-Hold)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.ylim([-1.2, 1.2])
plt.grid(True)

plt.tight_layout()
plt.show()
