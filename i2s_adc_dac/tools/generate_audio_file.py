from __future__ import print_function

import os
import struct
import wave
from builtins import range


# def get_wave_array_str(filename, target_bits):
#     wave_read = wave.open(filename, 'r')
#     array_str = ''
#     nchannels, sampwidth, framerate, nframes, comptype, compname = wave_read.getparams()
#     sampwidth *= 8
#     for i in range(wave_read.getnframes()):
#         val, = struct.unpack('<H', wave_read.readframes(1))
#         scale_val = (1 << target_bits) - 1
#         cur_lim   = (1 << sampwidth) - 1
#         # scale current data to 8-bit data
#         val       = val * scale_val / cur_lim
#         val       = int(val + ((scale_val + 1) // 2)) & scale_val
#         array_str += '0x%x, ' % (val)
#         if (i + 1) % 16 == 0:
#             array_str += '\n'
#     return array_str


# def gen_wave_table(wav_file_list, target_file_name, scale_bits=8):
#     with open(target_file_name, 'w') as audio_table:
#         print('#include <stdio.h>', file=audio_table)
#         print('const unsigned char audio_table[] = {', file=audio_table)
#         for wav in wav_file_list:
#             print('processing: {}'.format(wav))
#             print(get_wave_array_str(filename=wav, target_bits=scale_bits), file=audio_table)
#         print('};\n', file=audio_table)
#     print('Done...')


# if __name__ == '__main__':
#     print('Generating audio array...')
#     wav_list = []
#     for filename in os.listdir('./'):
#         if filename.endswith('.wav'):
#             wav_list.append(filename)
#     gen_wave_table(wav_file_list=wav_list, target_file_name='audio_example_file.h')



#install pyserial
import serial
import serial.tools.list_ports
import struct

baud = 115200
print("Serial ports:")

ports = serial.tools.list_ports.comports(include_links=False)

if len(ports) > 0:
    for port in ports:
        print(port.device)

    # on établit la communication série
    arduino = serial.Serial(ports[0].device, baud, timeout=1)

    max_samples = 240000
    sample_size = 2
    bufferlength = 512 * sample_size
    with open("/home/laura/esp/i2s_adc_dac/tools/test_recording", "wb") as f:
        while True:
            f.write(arduino.read(bufferlength))
            max_samples -= bufferlength / sample_size
            if max_samples < 0:
                break
