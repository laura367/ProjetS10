#!/usr/bin/python3
# -*- coding: utf-8 -*- 



from pydub import AudioSegment
import os,sys
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
from tempfile import mktemp
import numpy as np
from scipy.fftpack import fft,fftfreq
from scipy.signal import lfilter, butter
import wave #enable to get framerate
from scipy.signal import wiener


# file download from yt and convertion from w4a to wav via convertio
wname = 'son_lacrymo_save_test-24-of-49.wav'  # use temporary file
 # convert to wav
FS, data = wavfile.read(wname)  # read wav file, FS = samplerate
wf = wave.open(wname,'rb')
print(data.shape)
#(23439152, 2) => 23439152/479232 = 49 times for the split
samples = data.shape[0]
limit = int((len(data)/2)-1)
print('SAMPLES = ', samples)
print('FS = ', FS)


pre_emphasis = 0.97
emphasized_signal = np.append(data[0], data[1:] - pre_emphasis * data[:-1])

framerate = wf.getframerate()
print('framerate = ',framerate)
#48000
time_sig = np.linspace(1,len(data))
# print('signal_wave',len(signal_wav))
# print('time',len(time_sig))

# --------------------------plot all frequency spectrum


datafft = fft(data)
fftabs=abs(datafft)
freqs = fftfreq(samples,1/FS)
print("FREQS", freqs)
print('test pour freqs cibles', freqs)
print('frequencies = ',freqs.shape)
freqs_target = freqs[-20200:-15000]
print('fft = ',fftabs.shape)
# plt.subplot(2,1,1)
# plt.plot(freqs, fftabs)
# plt.title("Frequency spectrum of %s" % wname)
# plt.xlabel('frequency in Hz')
# plt.ylabel('amplitude')

b,a = butter(3, 1000/(FS*2), btype='highpass')  
filteredSignal = lfilter(b,a,data) 
filteredSignal_target = filteredSignal[-20200:-15000]
# plt.subplot(2,1,2)
# plt.plot(filteredSignal)
# plt.title("Signal filtered" )
# plt.xlabel('samples time')
# plt.ylabel('amplitude')
# plt.show()

import sys
import os
import subprocess
import json
import math








GuassianNoise = np.random.rand(len(time_sig))  

#NewSound = GuassianNoise + data[int(239*FS):int(240*FS)]  
#write("New-Sound-Added-With-Guassian-Noise.wav", FS, NewSound) 
 


# plt.plot(filteredSignal)
# plt.title("Signal filtered" )
# plt.xlabel('samples time')
# plt.ylabel('amplitude')

# plotting
fig,ax = plt.subplots()
plt.plot(freqs_target,filteredSignal_target,linewidth=5)
plt.title('filtered signal')
plt.ylabel('Amplitude')
plt.xlabel('Frequency [Hz]')
plt.show()

# ---------------------signal plot for the lacrymogene bomb trigger

# plt.plot(data[238*FS:240*FS]) #plot from 3min 55 minute to 4 min
# plt.xlabel('samples')
# plt.ylabel('Frequency Hz')
# # plt.plot(data[-20500:-15000])
# plt.show()
"""

# --------------------------Filtering with a bandpass


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    # Sample rate and desired cutoff frequencies (in Hz).
    lowcut = 500.0
    highcut = 1250.0

    # Plot the frequency response for a few different orders.
    plt.figure(1)
    plt.clf()
    for order in [3, 6, 9]:
        b, a = butter_bandpass(lowcut, highcut, FS, order=order)
        w, h = freqz(b, a, worN=2000)
        plt.plot((FS * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

    plt.plot([0, 0.5 * FS], [np.sqrt(0.5), np.sqrt(0.5)],
             '--', label='sqrt(0.5)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='best')

    # Filter a noisy signal.
    T = (1/44.1E3)
    nsamples = T * FS
    t = np.linspace(0, T, nsamples, endpoint=False)
    a = 0.02
    f0 = 600.0

    plt.figure(2)
    plt.clf()
    plt.plot(time_sig, signal_wav, label='Noisy signal')

    y = butter_bandpass_filter(data, lowcut, highcut, FS, order=6)
    plt.plot(time_sig, y, label='Filtered signal (%g Hz)' % f0)
    plt.xlabel('time (seconds)')
    plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')

    plt.show()
"""
