# ProjetS10


## ENV activation
* $ cd projets10/bin/
* $ . activate 


## ENV deactivation
$ deactivate

####  All the Venv criteria are in the requirements.txt

## Using ESP-IDF
* For the installation follow the following link : https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html
* In terminal

* $ cd
* cd esp/esp-idf/
## Enable to build the project from the esp folder
* $ . $HOME/esp/esp-idf/export.sh 
## Enable the permissions for using the ttyUSB0 port
## connect the esp32 to the computer
* $ sudo su 
* $ cd /
* $ cd /dev/
* $ chown user ttyUSB0
* $ exit
## Go to the working folder
* $ cd ~/esp/
## To test the recoring go first in the i2s/ folder then to access to the flash memory work with i2s_adc_dac_with_interruption_and_bugs_V2/ folder
## To make the acquisition when the valve opens do
* $ cd i2s_adc_dac_with_interruption_and_bugs_V2/
## build the project
* $ idf.py build
## flash the esp and show the monitor to see the result
* $ make flash monitor 
### Or you can do ---> But the first solution is better (make => verify and compute then flash and show the monitor) 
* $ idf.py -p /dev/ttyUSB0  flash monitor

* The monitor enble to see the outpout data and the code prints
* to quit the monitor ---> Do CTRL + ALT GR + ]


## TEST WITH AN ELECTRET MIC

## WIRING WITH THE I2S MODULE, ESP32, THE ELECTRET MIC

#### ----------------------GND MIC - GND I2S - GND ESP32 - GND BTN - LED RESISTOR - LED BUTTON
##
#### ----------------------5V ESP32 - 5V I2S - Resistor
##
#### ----------------------MIC (+) - ESP32 GPIO 36 (PIN VP and corresponding to the CHANNEL_0) - Resistor  
##
#### ----------------------TX ESP32 - RX I2S Module
##
#### ----------------------RX ESP32 - TX I2S Module
##
#### ----------------------ESP32 GPIO 22 LED - RESISTOR  
##
#### ----------------------ESP32 GPIO 15 BUTTON - RESISTOR 



## Configuration of the development framework
* Partition Table ---> Partition Table (Custom partition table CSV) -->Custom Partition table CVS ---> Copy and paste the name of the csv file in your working folder
* Serial Flasher Configuration ---> Set the flash size to 4Mb
* configure the serial baud to 115200 baud
##
### Descrption of the Repository
* To test the Bluetooth you can build in the bt_discovery
* To test with the Arduino IDE you can use the program in the esp_btn_led including the interruption simulating the openong of the valve
* The sounds folder is corresponding to the tests audio files
* The Results folder is corresponding to the results of audio filtered
