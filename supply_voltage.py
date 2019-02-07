import nibo

nibo.Start()

for i in range(1, 4):
    response = nibo.Send('request get 2')
    print("response: '{r}'".format(r = response))
    nibo.Delay(1000)

nibo.Stop()