import nibo

waitTimeMilliseconds = 100

nibo.Start()

try:
    while(1):
        a, b = nibo.GetPushButton()
        print('Button: A = %s, B = %s'%(a, b))
        nibo.Delay(waitTimeMilliseconds)

except KeyboardInterrupt:
    print('\nexit')

nibo.Stop()