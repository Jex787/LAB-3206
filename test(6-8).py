import numpy as np
import matplotlib.pyplot as plt

data_input = input("Enter a binary digit: ")
x = [int(bit) for bit in data_input if bit in '01']

bp = 1e-6
samples = 100
t_bit = np.linspace(0, bp, samples)
t_total = np.linspace(0, bp * len(x), len(x) * samples)

digital_signal = np.repeat(x, samples)

# ASK
# ----------------------------------------
# A1 = 10
# A2 = 5
# f = (1 / bp) * 10
# carrier = np.cos(2*np.pi*f*t_bit)
# modulated = []
# for bit in x:
#     amplitude = A1 if bit==1 else A2
#     wave = amplitude * carrier
#     modulated += list(wave)
# recoverd = []
# for i in range(0, len(modulated), samples):
#     segment = modulated[i:i+samples]
#     product = np.multiply(segment, carrier)
#     area = np.trapz(product, t_bit)
#     bit = 1 if (2*area/bp) > 7.5 else 0
#     recoverd.append(bit)
# ------------------------------------------

# FSK
# ------------------------------------------
# A = 5
# f1 = 10/bp
# f2 = 5/bp
# modulated = []
# for bit in x:
#     freq = f1 if bit==1 else f2
#     wave = A * np.cos(2*np.pi*freq*t_bit)
#     modulated += list(wave)
# recoverd = []
# for i in range(0, len(modulated), samples):
#     segment = modulated[i:i+samples]
#     product1 = np.multiply(segment, np.cos(2*np.pi*f1*t_bit))
#     product2 = np.multiply(segment, np.cos(2*np.pi*f2*t_bit))
#     area1 = np.trapz(product1, t_bit)
#     area2 = np.trapz(product2, t_bit)
#     bit = 1 if area1>area2 else 0
#     recoverd.append(bit)
# ---------------------------------------------

# PSK
# ---------------------------------------------
# A = 5
# fc = 2/bp
# carrier = np.cos(2*np.pi*fc*t_bit)
# modulated = []
# for bit in x:
#     wave = A * carrier
#     if bit == 0:
#         wave = -wave
#     modulated += list(wave)
# recoverd = []
# for i in range(0, len(modulated), samples):
#     segment = modulated[i:i+samples]
#     probuct = np.multiply(segment, carrier)
#     area = np.trapz(probuct, t_bit)
#     bit = 1 if area>0 else 0
#     recoverd.append(bit)
# ------------------------------------------

recoverd_signal = np.repeat(recoverd, samples)

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t_total, digital_signal, linewidth=2.5)
plt.title("Transmited Information as Digital Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-0.5, 1.5)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t_total, modulated)
plt.title("wavefrom for (ask/fsk/psk) Modulation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_total, recoverd_signal, linewidth=2.5)
plt.title("Recoverd Information as Digital Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim(-0.5, 1.5)
plt.grid(True)

plt.tight_layout()
plt.show()

print("Transmited Data: ", x)
print("Recived Data: ", recoverd)