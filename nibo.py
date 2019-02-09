import serial
import time
import threading
import re
import enum 

try:
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT, initial = 0)
        GPIO.setup(22, GPIO.OUT, initial = 0)

except RuntimeError as err:
        # this is only for testing - This module can only be run on a Raspberry Pi!
        print(err)

# Register NIBObee
#  0: [r ] BOT ID = 0x4e62
#  1: [r ] Version
#  2: [r ] Supply Voltage [mV]
#  3: [rw] LEDs
#  4: [r ] Sense
#  6: [rw] Motor Mode 
#  7: [rw] Motor PWM L 
#  8: [rw] Motor PWM R 
#  9: [rw] Motor PID L 
# 10: [rw] Motor PID R 
# 13: [r ] Odometry L 
# 14: [r ] Odometry R 
# 16: [r ] Line C
# 17: [r ] Line L
# 18: [r ] Line R

# This can be used to enable printing the communication to the console
PrintCommunication = False

class LED(enum.Enum):
        YellowLeft = 1
        RedLeft = 2
        RedRight = 4
        YellowRight = 8
        GreenUpper = 16
        RedUpper = 32

class Feeler(enum.Enum):
        LeftOuter = 1
        LeftInner = 2
        RightOuter = 16
        RightInner = 32

try:
        ser = serial.Serial('/dev/serial0', 9600)
        ser.timeout = 1        
except serial.SerialException as err:
        # this is only for testing
        print(err) 

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
        global PrintCommunication

        echo = []
        response = []
        echoReceived.clear()
        responseReceived.clear()
        if PrintCommunication : print('<<', command)
        ser.write(command.encode('utf-8'))
        ser.write(b'\r\n')
        echoReceived.wait(5)
        # sEcho = ''.join([x.decode('utf-8') for x in echo])
        # if PrintCommunication : print('echo: ', sEcho)
        responseReceived.wait(5)
        sResponse = ''.join([x.decode('utf-8') for x in response])
        if PrintCommunication : print('>>', sResponse)
        return sResponse

def SetGPIO(pin, value):
        GPIO.output(pin, value)

def GetSupplyVoltageMillivolt():
        respone = Send('request get 2')
        return int(re.findall(r'\d+', respone)[1])

def GetLEDMask():        
        # TODO: Add upper GPIO LEDs
        respone = Send('request get 3')
        return int(re.findall(r'\d+', respone)[1])

def SetLEDMask(mask):
        # TODO: Add upper GPIO LEDs
        Send('request set 3, %s'%(mask))

def SetLED(led, powerStatus):
        if led == LED.GreenUpper:
                SetGPIO(18, powerStatus)
        elif led == LED.RedUpper:
                SetGPIO(22, powerStatus)
        else:
                ledMask = GetLEDMask()
                if powerStatus == 0:
                        ledMask &= ~led.value
                else:
                        ledMask |= led.value
                Send('request set 3, %s'%(ledMask))

def GetFeeler():
        respone = Send('request get 4')
        feelerMask = int(re.findall(r'\d+', respone)[1])
        flo = bool(feelerMask & Feeler.LeftOuter.value) 
        fli = bool(feelerMask & Feeler.LeftInner.value) 
        fro = bool(feelerMask & Feeler.RightOuter.value) 
        fri = bool(feelerMask & Feeler.RightInner.value) 
        return flo, fli, fro, fri

                