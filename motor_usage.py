import nibo

nibo.PrintCommunication = True

waitTimeMilliseconds = 100

nibo.Start()

nibo.SetMotorMode(3) # I believe this is PID

try:
    while(1):
        for speed in range(-100,101,25):
            nibo.SetMotors(speed,speed)
            nibo.Delay(1000)
        
        for speed in range(100,-101,-25):
            nibo.SetMotors(speed,speed)
            nibo.Delay(1000)

except KeyboardInterrupt:
    nibo.SetMotors(0,0)
    print('\nexit')

nibo.Stop()