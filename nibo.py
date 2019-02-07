import serial
import time
import threading

ser = serial.Serial('/dev/serial0', 9600)
ser.timeout = 1
stopReadThread = threading.Event()
responseReceived = threading.Event()
response = []

def ReadThread(waitTime):
        global stopReadThread
        while(stopReadThread.is_set() != True):
                sbyte = ser.read()                
                print(sbyte.decode(), end='', flush=True)

                if sbyte == b'\r' or sbyte == b'\n':
                    responseReceived.set()
                else :
                    response.append(sbyte)

                stopReadThread.wait(waitTime)

reader = threading.Thread(target = ReadThread, args= (0.001, ))

def Start():
        reader.start()
        time.sleep(0.1)

def Stop():
        global stopReadThread
        stopReadThread.set()

def Delay(milliseconds):
    time.sleep(milliseconds / 1000.0)

def Send(command):
    global response
    response = []
    responseReceived.clear()
    ser.write(command.encode('utf-8'))
    ser.write(b'\r\n')
    responseReceived.wait(5)
    return ''.join([x.decode() for x in response])

def GetSupplyVoltageMillivolt():
    # TODO
    Send('')