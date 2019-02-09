import nibo

waitTimeMilliseconds = 100

nibo.Start()

while(1):
    flo, fli, fro, fri = nibo.GetFeeler()
    print('Feeler: LO = %s, LI = %s, RO = %s, RI = %s'%(flo, fli, fro, fri))
    nibo.Delay(waitTimeMilliseconds)

nibo.Stop()