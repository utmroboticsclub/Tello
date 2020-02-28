# Iterative Face Follow

## Objective
The objective of this project is to control Tello Drone using various control methods.
These methods include:
- Manual (Logitech G710)
- Autonomous through Feedback(Following a Face)
- Preplanned Motion Planning and Following(Flying a preplanned curve)
- Races (Just a dream)
## Linux Setup

### Requirements
Install Python

``` bash
sudo apt-get install python2.7 python-pip -y
sudo pip install --upgrade pip
```

The following are required to compile the h264decoder python package
``` bash
sudo pip install cmake

# install dependencies
sudo apt-get install libboost-all-dev -y
sudo apt-get install libavcodec-dev -y
sudo apt-get install libswscale-dev -y
sudo apt-get install python-matplotlib -y
sudo apt-get install python-imaging-tk
```
The following are re
## Running
- Ensure A G710 Joystick is plugged into your motor.