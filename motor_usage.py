import nibo

nibo.PrintCommunication = False

waitTimeMilliseconds = 100

nibo.Start()

nibo.SetMotorMode(3) # I believe this is PID

try:
    while(1):
        for speed in range(-100,101,25):
            nibo.SetMotors(speed,speed)           
            nibo.Delay(1000)
            odoLeft, odoRight = nibo.GetOdometry()
            print('Odometry - Left = %s, Right = %s'%(odoLeft, odoRight))

        for speed in range(100,-101,-25):
            nibo.SetMotors(speed,speed)
            nibo.Delay(1000)
            odoLeft, odoRight = nibo.GetOdometry()
            print('Odometry - Left = %s, Right = %s'%(odoLeft, odoRight))

except KeyboardInterrupt:
    nibo.SetMotors(0,0)
    print('\nexit')

nibo.Stop()