import socket
import sys,os

serverMACAddress = '40:F5:20:71:D0:3E'
USB = open( "/dev/ttyUSB0")
port = 3333
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send("coucoud")
s.close()
