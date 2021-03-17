#!/usr/bin/python3
# -*- coding: utf-8 -*- 



from pydub import AudioSegment
import os,sys, wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
from tempfile import mktemp
import numpy as np
from scipy.fftpack import fft,fftfreq
from scipy.signal import lfilter, butter
import wave #enable to get framerate
from scipy.signal import wiener
from scipy.signal import remez
from scipy import signal





# 'Son-test-lacrymo.wav' first test with wind
#digital testing with audio file took from the voice recorder of a smartphone
# to calculate the remain volume with 'Calcul-volume.wav' 
wname = 'Test_environ_1m_avec_voiture.wav'  # Test-voix-ecart.wav' test with sound taer gas sprayer + wind + human voice + distance of 30 cm
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
print('FRAMERATE = ',framerate)
#48000
time_sig = np.linspace(1,len(data))
# print('signal_wave',len(signal_wav))
# print('time',len(time_sig))

# --------------------------plot all frequency spectrum


datafft = fft(data)
print('datafft',datafft)
fftabs=abs(datafft)
freqs = fftfreq(samples,1/FS)
print("FREQS", freqs)
print('test pour freqs cibles', freqs)
print('frequencies = ',freqs.shape)
plt.subplot(2,1,1)
# plt.plot(freqs, fftabs)
# plt.title("Frequency spectrum of %s" % wname)
# plt.xlabel('frequency in Hz')
# plt.ylabel('amplitude')



#high pass filter enhanced the sound quality
#Naturally used for sound amplification
b,a = butter(6, 1000/(FS*2), btype='highpass')  
filteredSignal = lfilter(b,a,data) 
# plt.subplot(2,1,2)
# plt.plot(filteredSignal)
# plt.title("Signal filtered" )
# plt.xlabel('samples time')
# plt.ylabel('amplitude')
# plt.show()


fgust = signal.filtfilt(b, a, data, method="gust")
fpad = signal.filtfilt(b, a, data, padlen=50)
# plt.plot(data, 'k-', label='input')
# plt.plot(fgust, 'b-', linewidth=4, label='gust method')
# plt.plot(fpad, 'c-', linewidth=1.5, label='pad method')
# plt.legend(loc='best')
# plt.show()
# plt.plot(fpad, 'c-', linewidth=1.5, label='pad method')
# plt.legend(loc='best')
# plt.show()




lowcut_tgs = 9000#15000
highcut_tgs= 10000#16000
FRAME_RATE = framerate


def butter_bandpass_tgs(lowcut, highcut, fs, order=3):
    nyq = 0.5 * FS
    low_tgs = lowcut_tgs/ nyq
    high_tgs= highcut_tgs / nyq
    b2, a2 = butter(order, [low_tgs, high_tgs], btype='bandpass')
    return b2, a2

def butter_bandpass_filter_tgs(data, lowcut, highcut, fs, order=3):
    b2, a2 = butter_bandpass_tgs(lowcut_tgs, highcut_tgs, FS, order=order)
    y = lfilter(b2, a2, data)
    return y

def bandpass_filter_tgs(buffer):
    return butter_bandpass_filter_tgs(data, lowcut_tgs, highcut_tgs, FRAME_RATE, order=3)


filtered_sprayer = np.apply_along_axis(bandpass_filter_tgs, 0, data).astype('int16')

#for the  voice sound
#wavfile.write(os.path.join("/home/laura/Bureau/ProjetS10/traitement_wav", f'secouage_for_lacrymo'), FS, filtered_sprayer)


