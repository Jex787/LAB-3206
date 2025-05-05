import numpy as np
import matplotlib.pyplot as plt

# --- User Input ---
binary_input = input("Enter binary data (e.g., 10100101): ")
x = np.array([int(bit) for bit in binary_input])
print("Input bits:", x)

# --- Convert to Polar Form ---
p = np.where(x == 0, -1, 1)

# Separate Even and Odd Indexed Bits
even_seq = p[::2]
odd_seq = p[1::2]

# Time vector
bit_duration = 2
t = np.arange(0, len(p), 0.01)
even_ps = np.zeros_like(t)
odd_ps = np.zeros_like(t)

# --- Corrected NRZ Polar Signal Generation ---

# Even bits signal
for i in range(len(even_seq)):
    start = int((bit_duration * i) / 0.01)
    end = int((bit_duration * (i + 1)) / 0.01)
    even_ps[start:end] = even_seq[i]

# Odd bits signal
for i in range(len(odd_seq)):
    start = int((bit_duration * i) / 0.01)
    end = int((bit_duration * (i + 1)) / 0.01)
    odd_ps[start:end] = odd_seq[i]

# --- Plot 1: NRZ Polar Line Coded Signal ---
plt.figure(figsize=(10, 6))

plt.subplot(2,1,1)
plt.plot(t, even_ps, 'r')
plt.title('NRZ Polar Line Coded Signal - Even Bits')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t, odd_ps, 'b')
plt.title('NRZ Polar Line Coded Signal - Odd Bits')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Plot 2: Carrier Signals ---
c1 = np.cos(2 * np.pi * 1 * t)
c2 = np.sin(2 * np.pi * 1 * t)

plt.figure(figsize=(10, 4))

plt.subplot(2,1,1)
plt.plot(t, c1, 'r')
plt.title('Cosine Carrier Signal')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t, c2, 'b')
plt.title('Sine Carrier Signal')
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Plot 3: QPSK Modulated Signal ---
r1 = even_ps * c1
r2 = odd_ps * c2
qpsk = r1 - r2

plt.figure(figsize=(10, 6))

plt.subplot(3,1,1)
plt.plot(t, r1, 'r')
plt.title('I-component (Even × Cosine)')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, r2, 'b')
plt.title('Q-component (Odd × Sine)')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, qpsk, 'k')
plt.title('QPSK Signal (I - Q)')
plt.xlabel('Time')
plt.grid(True)

plt.tight_layout()
plt.show()
