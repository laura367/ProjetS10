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
from scipy.fftpack import fft,fftfreq
from scipy.signal import lfilter, butter
import wave #enable to get framerate
from scipy.signal import wiener
from scipy.signal import remez
from scipy import signal



'''
You have to put the audio file in the same folder as your python file
You can work either with wav files or mp3
Do not forget to change the path when you creating the wav file filtered
'''

# 'Son-test-lacrymo.wav' first test with wind
#digital testing with audio file took from the voice recorder of a smartphone
# to calculate the remain volume with 'Calcul-volume.wav' 
wname = 'Test_1m.wav'  # Test-voix-ecart.wav' test with sound taer gas sprayer + wind + human voice + distance of 30 cm
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

# --------------------------plot all frequency spectrum


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
# tps = 1/int(frequencies)
#print(tps)

# --------------------------Remaining volume in the tear gas sprayer tank
for temps in range(0,int(duration)):
   
    flow_rate = 30/duration
    print(temps)
    # print(flow_rate)
#Regarding the volume of the tear gas sprayer test which is 30 mL, and the time measure until 
# the ta,k is empty, which about 7 seconds we can measure the volume flow rate which will be 4.2 mL/s 
    volume = flow_rate*temps/1000
    volume2 = flow_rate/frequencies[0]

print('REMAINING VOLUME : {0}mL'.format(volume))
print('VERIFICATION REMAINING VOLUME : {0}mL'.format(volume2))
# -------------------------Plot of the FFT signal

plt.subplot(2,1,1)
plt.plot(freqs, fftabs)
plt.title("Frequency spectrum of %s" % wname)
plt.xlabel('frequency in Hz')
plt.ylabel('amplitude')

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
wavfile.write(os.path.join("/home/laura/Bureau/ProjetS10/traitement_wav", f'tgs_processing_test2'), FS, filtered_sprayer)


