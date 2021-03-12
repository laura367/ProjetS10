# ProjetS10

## ENV activation


$ cd projets10/bin/
$ . activate 


## ENV deactivation
$ deactivate

## Using ESP-IDF
* For the installation follow the following link : https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html
* In terminal

$ cd
$ cd esp/esp-idf/
## Enable to build the project from the esp folder
$ . $HOME/esp/esp-idf/export.sh 
## Enable the permissions for using the ttyUSB0 port
## connect the esp32 to the computer
$ sudo su 
$ cd /
$ cd /dev/
$ chown user ttyUSB0
$ exit
## Go to the working folder
$ cd ~/esp/
## All the validate folders are here
## To make the acquisition do
$ cd i2s_adc_dac_with_interruption_and_bugs/
## build the project
$ idf.py build
## flash the esp and show the monitor to see the result
$ make flash monitor 
### Or you can do ---> But the first solution is better (make => verify and compute then flash and show the monitor) 
$ idf.py -p /dev/ttyUSB0  flash monitor

* The monitor enble to see the outpout data and the code prints
* to quit the monitor ---> Do CTRL + ALT GR + ]

#
# WIRING WITH THE I2S MODULE, ESP32, THE MIC

### ----------------------GND MIC - GND I2S - GND ESP32 - GND BTN - LED RESISTOR - LED BUTTON
##
### ----------------------5V ESP32 - 5V I2S - Resistor
##
### ----------------------MIC (+) - ESP32 GPIO 36 (PIN VP) - Resistor  
##
### ----------------------TX ESP32 - RX I2S Module
##
### ----------------------RX ESP32 - TX I2S Module
##
## ----------------------ESP32 GPIO 22 LED - RESISTOR  
##
## ----------------------ESP32 GPIO 15 BUTTON - RESISTOR 



## Configuration of the development framework
* Partition Table ---> Partition Table (Custom partition table CSV) -->Custom Partition table CVS ---> Copy and paste the name of the csv file in your working folder
* Serial Flasher Configuration ---> Set the flash size to 4Mb
##
##
##
##

