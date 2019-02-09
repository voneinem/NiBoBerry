import nibo
from nibo import LED

nibo.PrintCommunication = True

nibo.Start()

nibo.SetLEDMask(0)
nibo.Delay(1000)
nibo.SetLEDMask(15)
nibo.Delay(1000)
nibo.SetLEDMask(0)

for i in range(1, 5):

    waitTimeMilliseconds = 100

    nibo.SetLED(LED.YellowLeft, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(LED.YellowLeft, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(LED.YellowRight, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(LED.YellowRight, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(LED.RedLeft, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(LED.RedLeft, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(LED.RedRight, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(LED.RedRight, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(LED.RedUpper, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(LED.RedUpper, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(LED.GreenUpper, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(LED.GreenUpper, 0)
    nibo.Delay(waitTimeMilliseconds)

nibo.Stop()