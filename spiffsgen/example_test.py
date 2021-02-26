from __future__ import print_function
from scipy.io import wavfile
import hashlib
import os
import numpy as np

import ttfw_idf


@ttfw_idf.idf_example_test(env_tag='Example_GENERIC')
def test_examples_spiffsgen(env, extra_data):
    # Test with default build configurations
    dut = env.get_dut('spiffsgen', 'examples/storage/spiffsgen', dut_class=ttfw_idf.ESP32DUT)
    dut.start_app()

    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spiffs_image')
    audio = wavfile.read("hello.wav")
    # Expect hello.txt is read successfully
    with open(os.path.join(base_dir, audio), 'r') as wav_file:
        dut.expect('Read from  hello.wav ' + wav_file().rstrip())

    # Expect alice.txt MD5 hash is computed accurately
    with open(os.path.join(base_dir, 'sub', 'alice.txt'), 'rb') as alice_txt:
        coucou_audio = hashlib.md5(alice_txt.read()).hexdigest()
        dut.expect('Computed MD5 hash of hello.wav: ' + coucou_audio)

    wavfile.write('after_storage.wav', 44100, wav_file.astype(np.int16))


if __name__ == '__main__':
    test_examples_spiffsgen()
    
