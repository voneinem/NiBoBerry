import nibo

nibo.Start()

for i in range(1, 10):

    nibo.SetLED(nibo.LED.YellowLeft, nibo.Power.on)
    nibo.Delay(1000)
    nibo.SetLED(nibo.LED.YellowLeft, nibo.Power.off)
    nibo.Delay(1000)

nibo.Stop()