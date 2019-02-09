# NiBoBerry
Fun with NIBObee Berry (nicai systems)

I just got my [NIBObee Berry](http://www.nicai-systems.com/en/robotics/nibobee/berry) up and running.
Now I'm going to share my stuff here for anybody that might be interested.

## Projects

### Simple serial communication 

[ledserial.py](./ledserial.py)

This script allows to send commands and receive replys from RPi to NIBObee.

More about the serial protocol [here](http://www.nibo-roboter.de/wiki/Nibo_Serial_Protocol).

### Python API for the NIBObee sensors and actors

Import [nibo.py](./nibo.py) in order to use the API functions.
```python
from nibo import *
```

#### Supply Voltage

A first usage example is  [supply_voltage.py](./supply_voltage.py).

```python
voltageMillivolt = nibo.GetSupplyVoltageMillivolt()
```

#### LEDs

A second usage example is [led_usage.py](./led_usage.py).
For this one I created simple unit tests in [test_nibo.py](./test_nibo.py)

```python
# allow to omit nibo. of LED enum
from nibo import LED

# get the binary mask for all LEDs once
ledMask = nibo.GetLEDMask()

# set the binary mask for all LEDs once
nibo.SetLEDMask(0)

# switch left yellow LED on
nibo.SetLED(LED.YellowLeft, 1)

# switch left yellow LED off
nibo.SetLED(LED.YellowLeft, 0)
```

#### Feelers

An example how to get the feeler status is [feelers_usage.py](./feelers_usage.py).

```python
    flo, fli, fro, fri = nibo.GetFeeler()
    print('LO = %s, LI = %s, RO = %s, RI = %s'%(flo, fli, fro, fri))
```

#### Next step is support for the motors :)