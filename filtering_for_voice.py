#!/usr/bin/python3
# -*- coding: utf-8 -*- 

'''
Created for the shield project of the ANS Connect startup
by
Valier-Brasier Laura 
'''


from pydub import AudioSegment
import os,sys, wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
from tempfile import mktemp
from numpy import array, diff, where, split
import numpy as np
import soundfile
from scipy.fftpack import fft,fftfreq
from scipy.signal import lfilter, butter
import wave #enable to get framerate
from scipy.signal import wiener
from scipy.signal import remez
from scipy import signal
# import pyaudio
remez(11, [0.1, 0.4], [1], type='hilbert')


# file download from yt and convertion from w4a to wav via convertio
# 'Son-test-lacrymo.wav' first test with wind
#digital testing with audio file took from the voice recorder of a smartphone
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
number_samples = len(data)
duration = round(number_samples/FS,2)
print('AUDIO DURATION : {0}s'.format(duration))


pre_emphasis = 0.97
emphasized_signal = np.append(data[0], data[1:] - pre_emphasis * data[:-1])

framerate = wf.getframerate()
print('FRAMERATE = ',framerate)
#48000
time_sig = np.linspace(1,len(data))
# print('signal_wave',len(signal_wav))
# print('time',len(time_sig))


def findPeak(magnitude_values, noise_level=2000):
    
    splitter = 0
    # zero out low values in the magnitude array to remove noise (if any)
    magnitude_values = np.asarray(magnitude_values)        
    low_values_indices = magnitude_values < noise_level  # Where values are low
    magnitude_values[low_values_indices] = 0  # All low values will be zero out
    
    indices = []
    
    flag_start_looking = False
    
    both_ends_indices = []
    
    length = len(magnitude_values)
    for i in range(length):
        if magnitude_values[i] != splitter:
            if not flag_start_looking:
                flag_start_looking = True
                both_ends_indices = [0, 0]
                both_ends_indices[0] = i
        else:
            if flag_start_looking:
                flag_start_looking = False
                both_ends_indices[1] = i
                # add both_ends_indices in to indices
                indices.append(both_ends_indices)
                
    return indices

def extractFrequency(indices, freq_threshold=200):
    
    extracted_freqs = []
    
    for index in indices:
        freqs_range = freqs[index[0]: index[1]]
        avg_freq = round(np.average(freqs_range))
        
        if avg_freq not in extracted_freqs:
            extracted_freqs.append(avg_freq)

    # group extracted frequency by nearby=freq_threshold (tolerate gaps=freq_threshold)
    group_similar_values = split(extracted_freqs, where(diff(extracted_freqs) > freq_threshold)[0]+1 )
    
    # calculate the average of similar value
    extracted_freqs = []
    for group in group_similar_values:
        extracted_freqs.append(round(np.average(group)))
    
    print("freq_components", extracted_freqs)
    return extracted_freqs


# -------------------------- FFT calculs 


datafft = fft(data)
print('datafft',datafft)
fftabs=abs(datafft)
freqs = fftfreq(samples,1/FS)
print("FREQS", freqs)
print('test pour freqs cibles', freqs)
print('frequencies = ',freqs.shape)
# freq_bins = arange(number_samples) * audio_samples/number_samples
# print('Frequency Length: ', len(freq_bins))
# print('Frequency bins: ', freq_bins)
normalization_data = datafft/FS
magnitude_values = normalization_data[range(len(datafft)//2)]
magnitude_values = np.abs(magnitude_values)
indices = findPeak(magnitude_values=magnitude_values, noise_level=200)
frequencies = extractFrequency(indices=indices)
print("**********************KOKO-DA!!!!!!!!!!!!!!!*****")
print("frequencies:", frequencies)



# --------------------------Remaining volume in the tear gas sprayer tank
tps = 1/int(frequencies[0])
print(tps)
volume = 60/frequencies[0]

print('REMAINING VOLUME : {0}mL'.format(volume))
# -------------------------Plot of the FFT signal

plt.subplot(2,1,1)
plt.plot(freqs, fftabs)
plt.title("Frequency spectrum of %s" % wname)
plt.xlabel('frequency in Hz')
plt.ylabel('amplitude')



#high pass filter enhanced the sound quality
#Naturally used for sound amplification
b,a = butter(6, 1000/(FS*2), btype='highpass')  
filteredSignal = lfilter(b,a,data) 
plt.subplot(2,1,2)
# plt.plot(filteredSignal)
# plt.title("Signal filtered" )
# plt.xlabel('samples time')
# plt.ylabel('amplitude')
# plt.show()


#Apply the  Gustafsson method
fgust = signal.filtfilt(b, a, data, method="gust")
#Apply the padding after the Gustafsson method
fpad = signal.filtfilt(b, a, data, padlen=50)
# plt.plot(data, 'k-', label='input')
# plt.plot(fgust, 'b-', linewidth=4, label='gust method')
# plt.plot(fpad, 'c-', linewidth=1.5, label='pad method')
# plt.legend(loc='best')
# plt.show()
plt.plot(fpad, 'c-', linewidth=1.5, label='pad method')
plt.legend(loc='best')
# plt.show()

lowcut_voice = 500
highcut_voice = 800



def butter_bandpass_voice(lowcut, highcut, fs, order=3):
    nyq = 0.5 * FS
    low_voice = lowcut_voice / nyq
    high_voice = highcut_voice / nyq
    b2, a2 = butter(order, [low_voice, high_voice], btype='bandpass')
    return b2, a2

def butter_bandpass_filter_voice(data, lowcut, highcut, fs, order=3):
    b2, a2 = butter_bandpass_voice(lowcut_voice, highcut_voice, FS, order=order)
    y = lfilter(b2, a2, data)
    return y

def bandpass_filter_voice(buffer):
    return butter_bandpass_filter_voice(data, lowcut_voice, highcut_voice, 44000, order=3)
filtered_voice = np.apply_along_axis(bandpass_filter_voice, 0, data).astype('int16')

#for the  voice sound
wavfile.write(os.path.join("/home/laura/Bureau/ProjetS10/traitement_wav", f'filtered_for_voice'), FS, filtered_voice)


