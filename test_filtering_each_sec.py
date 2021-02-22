#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import scipy.io.wavfile as wavfile
from scipy import *
import scipy 
from scipy.fftpack import fft,fftfreq
import numpy as np
from matplotlib import pyplot as plt

fs_rate, signal = wavfile.read("Test_environ_1m_avec_voiture_copie.wav")
#print ("Frequency sampling", fs_rate)
l_audio = len(signal.shape)
#print ("Channels", l_audio)
if l_audio == 2:
    signal = signal.sum(axis=1) / 2

signal2 = signal     
N = signal2.shape[0] #samples
#print ("Complete Samplings N", N)
secs = N / float(fs_rate)
#print ("secs", secs)
Ts = 1.0/fs_rate # sampling interval in time
#print ("Timestep between samples Ts", Ts)
t = np.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray

#FFT1 = abs(scipy.fft(signal2[0:44100]))
FFT2 = abs(fft(signal2[44100:88200]))
FFT3 = abs(fft(signal2[88200:132300]))
FFT4 = abs(fft(signal2[132300:176400]))
FFT5 = abs(fft(signal2[176400:220500]))

#FFT_side1 = FFT1[range(N//20)] # one side FFT range
FFT_side2 = FFT2[range(N//20)] # one side FFT range
FFT_side3 = FFT3[range(N//20)] # one side FFT range
FFT_side4 = FFT4[range(N//20)] # one side FFT range
FFT_side5 = FFT5[range(N//20)] # one side FFT range

#freqs1 = scipy.fftpack.fftfreq(signal2[0:44100].size, t[1]-t[0])
freqs2 = fftfreq(signal2[44100:88200].size, t[1]-t[0])
freqs3 = fftfreq(signal2[88200:132300].size, t[1]-t[0])
freqs4 = fftfreq(signal2[132300:176400].size, t[1]-t[0])
freqs5 = fftfreq(signal2[176400:220500].size, t[1]-t[0])

#fft_freqs = np.array(freqs)

#freqs_side1 = freqs1[range(N//20)] # one side frequency range
freqs_side2 = freqs2[range(N//20)] # one side frequency range
freqs_side3 = freqs3[range(N//20)] # one side frequency range
freqs_side4 = freqs4[range(N//20)] # one side frequency range
freqs_side5 = freqs5[range(N//20)] # one side frequency range


#fft_freqs_side = np.array(freqs_side)

#abs(FFT_side1)
abs(FFT_side2)
abs(FFT_side3)
abs(FFT_side4)
abs(FFT_side5)

for a in range(60):
    #FFT_side1[a] = 0
    FFT_side2[a] = 0
    FFT_side3[a] = 0
    FFT_side4[a] = 0
    FFT_side5[a] = 0

plt.subplot(611)
p1 = plt.plot(t, signal2, "r") # plotting the signal
plt.xlabel('Time')
plt.ylabel('Amplitude')

# plt.subplot(612)
# p3 = plt.plot(freqs_side1, FFT_side1, "b") # plotting the positive fft spectrum
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')


plt.subplot(613)
p3 = plt.plot(freqs_side2, FFT_side2, "g") # plotting the positive fft spectrum
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(614)
p3 = plt.plot(freqs_side3, FFT_side3, "g") # plotting the positive fft spectrum
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(615)
p3 = plt.plot(freqs_side4, FFT_side4, "g") # plotting the positive fft spectrum
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(616)
p3 = plt.plot(freqs_side5, FFT_side5, "g") # plotting the positive fft spectrum
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.show()