from scipy.io import wavfile
from scipy import signal
from scipy.signal import kaiserord, firwin, lfilter, freqz
import numpy as np
import matplotlib.pyplot as plt

# sr, x = wavfile.read('Test_environ_1m_avec_voiture_copie.wav')      # 16-bit mono 44.1 khz


# b = signal.firwin(101, cutoff=120, fs=sr, pass_zero=True)

# b, a = signal.butter(3, 0.05)
# x = signal.lfilter(b, a, x)

# wavfile.write('test2.wav', sr, x.astype(np.int16))

# fs, xbis = wavfile.read('test2.wav')   
# samples = xbis[0]
# ###############APplying a second filter to enhance voice

# b, a = signal.iirfilter(3, [2*np.pi*50, 2*np.pi*200], rs=60,
#                         btype='band', analog=True, ftype='cheby2')
# w, h = signal.freqs(b, a, xbis)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.semilogx(w / (2*np.pi*samples), 20 * np.log10(np.maximum(abs(h), 1e-5)))
# ax.set_title('Chebyshev Type II bandpass frequency response')
# ax.set_xlabel('Frequency [Hz]')
# ax.set_ylabel('Amplitude [dB]')
# ax.axis((10, 1000, -100, 10))
# ax.grid(which='both', axis='both')
# plt.show()


fs_rate, signal = wavfile.read("Test_environ_1m_avec_voiture_copie.wav")

nsamples = len(signal)
t = np.arange(nsamples) / fs_rate
print('T :',t)
# The Nyquist rate of the signal.
nyq_rate = fs_rate / 2.0

width = 5.0/nyq_rate

# The desired attenuation in the stop band, in dB.
ripple_db = 100.0 #60 good coef?

# Compute the order and Kaiser parameter for the FIR filter.
N, beta = kaiserord(ripple_db, width)

# The cutoff frequency of the filter.
cutoff_hz = 300.0 #10hz

# Use firwin with a Kaiser window to create a lowpass FIR filter.
taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

# Use lfilter to filter x with the FIR filter.
filtered_x = lfilter(taps, 1.0, signal)

#------------------------------------------------
# Plot the FIR filter coefficients.
#------------------------------------------------

plt.figure(1)
plt.plot(taps, 'bo-', linewidth=2)
plt.title('Filter Coefficients (%d taps)' % N)
plt.grid(True)

#------------------------------------------------
# Plot the magnitude response of the filter.
#------------------------------------------------

plt.figure(2)
plt.clf()
w, h = freqz(taps, worN=nsamples/2)  #worn = fs_rate/2
plt.plot((w/np.pi)*nyq_rate, np.absolute(h), linewidth=2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.title('Frequency Response')
plt.ylim(-0.05, 1.05)
plt.grid(True)

# Upper inset plot.
ax1 = plt.axes([0.42, 0.6, .45, .25])
plt.plot((w/np.pi)*nyq_rate, np.absolute(h), linewidth=2)
plt.xlim(0,8.0)
plt.ylim(0.9985, 1.001)
plt.grid(True)

# Lower inset plot
ax2 = plt.axes([0.42, 0.25, .45, .25])
plt.plot((w/np.pi)*nyq_rate, np.absolute(h), linewidth=2)
plt.xlim(12.0, 20.0)
plt.ylim(0.0, 0.0025)
plt.grid(True)

#------------------------------------------------
# Plot the original and filtered signals.
#------------------------------------------------

# The phase delay of the filtered signal.
delay = 0.5 * (N-1) / (fs_rate)

plt.figure(3)
# Plot the original signal.
plt.plot(t, signal)
# Plot the filtered signal, shifted to compensate for the phase delay.
plt.plot(t-delay, filtered_x, 'r-')

# Plot just the "good" part of the filtered signal.  The first N-1
# samples are "corrupted" by the initial conditions.
plt.plot(t[N-1:]-delay, filtered_x[N-1:], 'g', linewidth=4)

plt.xlabel('t')
plt.grid(True)

plt.show()


wavfile.write('implementation_fiir.wav', fs_rate, filtered_x.astype(np.int16))