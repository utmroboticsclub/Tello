import oi
import tello
import vision
import time

tello = Tello()
oi = OI()

def mainLoop():
    while True:
        time.sleep(3)
        print("Left: " ,oi.getLeftX(), oi.getLeftY())
        print("Right: ",oi.getRightX(), oi.getRightY())

if __name__ == "main":
    mainLoop()