# NiBoBerry

Fun with NIBObee Berry (nicai systems)

I just got my [NIBObee Berry](http://www.nicai-systems.com/en/robotics/nibobee/berry) up and running.
Now I'm going to share my stuff here for anybody who might be interested.

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

#### Push Button

An example how to get the upper push button status is [pushbutton_usage.py](./pushbutton_usage.py).

```python
a, b = nibo.GetPushButton()
print('Button: A = %s, B = %s'%(a, b))
```

#### Motors

An example how to use the motors is [motor_usage.py](./motor_usage.py).
More on the PID controller [here](http://www.nibo-roboter.de/wiki/NIBObee/Motorregelung).

```python
nibo.SetMotorMode(3) # I believe this is PID motor control using odometry
nibo.SetMotors(-42,42) # turn coutner clockwise
```

#### Odometry

An example how to use the motors is embedded in [motor_usage.py](./motor_usage.py).

```python
odoLeft, odoRight = nibo.GetOdometry()
print('Odometry - Left = %s, Right = %s'%(odoLeft, odoRight))
```

#### Video processing with OpenCV

I want the NIBOBee to follow a green ball.
First I compiled OpenCV on the RPi as described [here](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/).
This takes some time (hours)...
Next I combined [ball tracking](https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/) with [PiCamera](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/).
The result (work in progress) is in [ball_tracking_pi.py](./ball_tracking_pi.py).

#### Control the motors with the signal from the camera

The result is in [ball_tracking_pi.py](./ball_tracking_pi.py).
NIBOBerry will try to follow a green ball it sees.

if you add the following line before ```exit 0``` in your /etc/rc.local...

```bash
sudo python3 home/pi/ball_tracking_pi.py &
```

... NIBOBerry will start ball_tracking_pi.py during boot.
Once the programm is up and running the top green LED will be on.
At this point ball tracking is active and you can watch the video over http on port 5000 (given Nibo has WLAN and you know the IP).
Nibo will indicate the rough direction where it sees the ball via LEDs: yellow left, red left, ...
If both red LEDs are on Nibo has the ball right in front.

When you press button A Nibo will switch on the motors and start moving towards the ball.
You can be mean and move the ball somewhere else. Nibo should recognize and follow.
Have fun...
