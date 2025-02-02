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

##############################################################################################################""######################
#                                                   WITH WEINER FILTER
######################################################################################################################################
lowcut_voice = 100#15000
highcut_voice= 800#16000
FRAME_RATE = framerate

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
    return butter_bandpass_filter_voice(data, lowcut_voice, highcut_voice, FRAME_RATE, order=3)

y = wiener(datafft,10,0)
filtered_voice = np.apply_along_axis(bandpass_filter_voice, 0, y).astype('int16')

wavfile.write(os.path.join("/home/laura/Bureau/ProjetS10/traitement_wav", f'test_2_for_voice'), FS, filtered_voice)
