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

The following are required to compile the h264decoder python package and run
imaging.
``` bash

# install dependencies
sudo apt-get install libboost-all-dev -y
sudo apt-get install libavcodec-dev -y
sudo apt-get install libswscale-dev -y
sudo apt-get install python-matplotlib -y
sudo apt-get install python-imaging-tk
```

For your python dependencies, it is recommended to use venv:
Guide to using Venv on Linux: https://docs.python-guide.org/dev/virtualenvs/
Please name your venv "telloEnv", this way it is not picked up via our .gitignore
```
pip install cmake
pip install -r ./iterative_face_follow/requirements.txt
```

Set up lib264decoder (Probably not required, but if libh264 gives issues, perform this step.)
```

cd h264decoder
mkdir build
cd build
cmake ..
make

cp libh264decoder.so ../../

````
## Running
- Ensure A G710 Joystick is plugged into your motor.
- Connect to Tello WiFi Network
```
cd iterative_face_follow
python main.py
```