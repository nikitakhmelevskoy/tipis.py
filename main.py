import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

frequencies = [1, 2, 4, 8]

for freq in frequencies:
    harmonic_signal = np.sin(2 * np.pi * freq * t)

    digital_signal = np.heaviside(np.sin(2 * np.pi * freq * t), 0)

    harmonic_spectrum = np.fft.fft(harmonic_signal)

    digital_spectrum = np.fft.fft(digital_signal)

    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.plot(t, harmonic_signal)
    plt.title(f'Harmonic Signal: {freq} Hz')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(2, 2, 2)
    plt.plot(t, digital_signal)
    plt.title(f'Digital Signal (One-Pole Square Wave): {freq} Hz')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(2, 2, 3)
    plt.plot(np.abs(harmonic_spectrum))
    plt.title(f'Spectrum of Harmonic Signal: {freq} Hz')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.xticks(np.arange(start=0, stop=50, step=2))
    plt.xlim(0, 50)

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(digital_spectrum))
    plt.title(f'Spectrum of Digital Signal: {freq} Hz')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.xticks(np.arange(start=0, stop=50, step=2))
    plt.xlim(0, 50)

    plt.tight_layout()
    plt.show()