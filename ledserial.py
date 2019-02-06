import serial
import time
from threading import Thread

ser = serial.Serial('/dev/serial0', 9600)

def ReadThread(waitTime):
    while(1):
        sbyte = ser.read()
        print(sbyte.decode(), end='', flush=True)
        time.sleep(waitTime)

def Send(command):
    print("sending: " + command)
    ser.write(command.encode('utf-8'))
    ser.write(b'\r\n')

reader = Thread(target = ReadThread, args= (0.001, ))
reader.start()

time.sleep(1)

# ===================================================================

while(1):
    for mask in range(0,16):
        Send('request set 3,{mask}'.format(mask=mask))
        time.sleep(1)