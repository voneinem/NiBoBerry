import serial
import time
import threading

ser = serial.Serial('/dev/serial0', 9600)
ser.timeout = 1
stopReadThread = threading.Event()
echoReceived = threading.Event()
responseReceived = threading.Event()
echo = []
response = []

def ReadThread(waitTime):
        global stopReadThread
        global echoReceived
        global responseReceived
        global response
        while(stopReadThread.is_set() != True):
                sbyte = ser.read()                
                # print(sbyte.decode('utf-8'), end='', flush=True)

                if echoReceived.is_set() == False:
                        if sbyte == b'\n':
                                echoReceived.set()
                        else :
                                if sbyte != b'\r' : echo.append(sbyte)
                else:                        
                        if sbyte == b'\n':
                                responseReceived.set()
                        else :
                                if sbyte != b'\r' : response.append(sbyte)

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
    global echoReceived
    global responseReceived
    global response
    global echo
    echo = []
    response = []
    echoReceived.clear()
    responseReceived.clear()
    print('<<', command)
    ser.write(command.encode('utf-8'))
    ser.write(b'\r\n')
    echoReceived.wait(5)
    # sEcho = ''.join([x.decode('utf-8') for x in echo])
    # print('echo: ', sEcho)
    responseReceived.wait(5)
    sResponse = ''.join([x.decode('utf-8') for x in response])
    print('>>', sResponse)
    return sResponse

def GetSupplyVoltageMillivolt():
    respone = Send('request get 2')
    return respone