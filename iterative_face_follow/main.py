import oi as oiInterface
import tello
import vision
import time

tello = tello.Tello()
oi = oiInterface.OI()
visionController = vision.TelloVision(tello)

DEADZONE = 0.075
MANUAL = 0
TRACK_FACES = 1

def mainLoop():
    print("Main: Starting Program loop")
    enabled = True
    mode = MANUAL
    while True:
        oi.update()
        if enabled:
            if mode == MANUAL:
                manualControl()
            elif mode == TRACK_FACES:
                pass

def manualControl():
    '''
        Maps controller Axis to Tello Flight:
        Left X = left/right
        Left Y =  Forward/backward
        Right X = YAW
        Right Y =  Up/Down TODO: Move Y to trigger axis
    '''
    a = axisToPercent(oi.getLeftX())
    b = axisToPercent(oi.getLeftY())
    c = axisToPercent(oi.getRightY())
    d = axisToPercent(oi.getRightX())
    print("rc A,B,C,D:",a,b,c,d)
    print("response: ", tello.rc_move(a,b,c,d))
    time.sleep(0.05)
def axisToPercent(axisVal):
    if not axisVal > DEADZONE and not axisVal < -DEADZONE:
        return 0 
    return int(100*axisVal)

if __name__ == "__main__":
    mainLoop()