# ProjetS10

#--- ENV activation


cd projets10/bin/
. activate 


#--- ENV deactivation
deactivate

#--- Using ESP-IDF
In terminal

cd
cd esp/esp-idf/
#Enable to build the project from the esp folder
. $HOME/esp/esp-idf/export.sh 
#Enable the permissions for using the ttyUSB0 port
#connect the esp32 to the computer
sudo su 
cd /
cd /dev/
chown user ttyUSB0
exit
#Go to the working folder
cd ~/esp/
#All the validate folders are here
#To make the acquisition do
cd i2s_adc_dac/
#build the project
idf.py build
#flash the esp and show the monitor to see the result
idf.py -p /dev/ttyUSB0  flash monitor



#-- WIRING WITH THE I2S MODULE, ESP32, THE MIC

##----------------------GND MIC - GND I2S - GND ESP32
##
##----------------------5V ESP32 - 5V I2S - Resistor
##
##----------------------MIC (+) - ESP32 GPIO 36 (PIN VP) - Resistor  
##
##----------------------TX ESP32 - RX I2S Module
##
##----------------------RX ESP32 - TX I2S Module
##
##



##---Configuration of th edevelopment framwork
##Partition Table ---> Partition Table (Custom partition table CSV) -->Custom Partition table CVS
##
##
##
##
##

