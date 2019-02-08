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

A first usage example is  [supply_voltage.py](./supply_voltage.py).
