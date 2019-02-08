import nibo

nibo.Start()

nibo.SetLEDMask(0)
nibo.Delay(1000)
nibo.SetLEDMask(15)
nibo.Delay(1000)
nibo.SetLEDMask(0)

for i in range(1, 5):

    waitTimeMilliseconds = 100

    nibo.SetLED(nibo.LED.YellowLeft, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(nibo.LED.YellowLeft, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(nibo.LED.YellowRight, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(nibo.LED.YellowRight, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(nibo.LED.RedLeft, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(nibo.LED.RedLeft, 0)
    nibo.Delay(waitTimeMilliseconds)

    nibo.SetLED(nibo.LED.RedRight, 1)
    nibo.Delay(waitTimeMilliseconds)
    nibo.SetLED(nibo.LED.RedRight, 0)
    nibo.Delay(waitTimeMilliseconds)

nibo.Stop()