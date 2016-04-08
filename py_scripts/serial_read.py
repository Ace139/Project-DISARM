#!/usr/bin/env python3
import serial

connected = False

locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3','/dev/ttyACM0']

for device in locations:
    try:
        print("Trying...",device)
        ser = serial.Serial(device, 9600)
        break
    except:
        print("Failed to connect on",device)

while not connected:
    serin = ser.read()
    connected = True

text_file = open("env_log.txt", 'r+')

while True:
    if ser.inWaiting():
        x = ser.read()
        print(x) 
        text_file.write(x)
        if x=="\n":
             text_file.seek(0)
             text_file.truncate()
        text_file.flush()

text_file.close()
ser.close()