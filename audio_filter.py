import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, iirnotch, sosfiltfilt

# 1. Load the input signal (noisy audio file)
file_name = 'noisy_voice.wav'
sample_rate, noisy_data = wavfile.read(file_name)
t = np.arange(len(noisy_data)) / sample_rate

# 2. Notch Filter: Remove the 6000 Hz noise spike
nyquist = 0.5 * sample_rate
freq_to_remove = 6000.0 / nyquist
quality_factor = 30.0  
b_notch, a_notch = iirnotch(freq_to_remove, quality_factor)

notched_data = filtfilt(b_notch, a_notch, noisy_data)

# 3. Bandpass Filter: Isolate human voice frequencies (300 - 3400 Hz)
lowcut = 300.0
highcut = 3400.0
low = lowcut / nyquist
high = highcut / nyquist

# Use SOS (Second-Order Sections) for stability in the 10th-order filter
sos = butter(10, [low, high], btype='band', output='sos')
final_clean_data = sosfiltfilt(sos, notched_data)

# 4. Normalize the amplitude and save the output audio
max_val = np.max(np.abs(final_clean_data))
if max_val > 0:
    final_clean_data = np.int16(final_clean_data / max_val * 32767)
else:
    final_clean_data = np.int16(final_clean_data)

wavfile.write('recovered_voice.wav', sample_rate, final_clean_data)

# 5. Plot the time-domain response
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t[:2000], noisy_data[:2000], color='salmon')
plt.title("Input Signal (Noisy Voice)", fontweight='bold')
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(t[:2000], final_clean_data[:2000], color='teal')
plt.title("Output Signal (Recovered Voice via Notch & Bandpass Filters)", fontweight='bold')
plt.xlabel("Time (Seconds)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

print("Filtering complete. Output saved as 'recovered_voice.wav'")