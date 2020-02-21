import pygame

class OI:
    LEFT_X = 0
    LEFT_Y = 1
    RIGHT_X = 2
    RIGHT_Y = 3

    def __init__():
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def getLeftX():
        return self.controller.get_axis(LEFT_X)

    def getLeftY():
        return self.controller.get_axis(LEFT_Y)

    def getRightX():
        return self.controller.get_axis(RIGHT_X)

    def getRightY():
        return self.controller.get_axis(RIGHT_Y)
