from __future__ import print_function

import hashlib
import os

import ttfw_idf

FLASH_ADDR = '0x200000'
@ttfw_idf.idf_example_test(env_tag='Example_GENERIC')
def test_examples_spiffsgen(env, extra_data):
    # Test with default build configurations
    dut = env.get_dut('spiffsgen', 'examples/storage', dut_class=ttfw_idf.ESP32DUT)
    dut.start_app()

    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spiffs_image')

    # Expect hello.txt is read successfully
    with open(os.path.join(base_dir, FLASH_ADDR), 'r') as hello_txt:
        dut.expect('Read from hello.txt: ' + hello_txt.read().rstrip())

    # Expect alice.txt MD5 hash is computed accurately
    with open(os.path.join(base_dir, 'sub', FLASH_ADDR), 'rb') as alice_txt:
        alice_md5 = hashlib.md5(alice_txt.read()).hexdigest()
        dut.expect('Computed MD5 hash of alice.txt: ' + alice_md5)


if __name__ == '__main__':
    test_examples_spiffsgen()
