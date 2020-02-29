import pygame as pygame

LEFT_X = 0
LEFT_Y = 1
RIGHT_X = 2
RIGHT_Y = 3
class OI:


    def __init__(self):
        print("OI: Beginning initialization")
        pygame.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        joystick_count = pygame.joystick.get_count()
        print(joystick_count)
        
        if joystick_count == 0:
            print("JOYSTICK NOT FOUND")
            exit()
        self.controller = joysticks[0]
        self.controller.init()
        self.axisNum = self.controller.get_numaxes()
        self.buttonNum = self.controller.get_numbuttons()
        print("OI: Controller Axis Number:", self.axisNum)
        print("OI: Controller Button Number:", self.buttonNum)
        print("OI: Complete initialization")

    def update(self):
        pygame.event.get()
        '''for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Close the program any way you want, or troll users who want to close your program.
                raise SystemExit
            '''
    def getLeftX(self):
        return self.controller.get_axis(LEFT_X)

    def getLeftY(self):
        return -self.controller.get_axis(LEFT_Y)

    def getRightX(self):
        return self.controller.get_axis(RIGHT_X)

    def getRightY(self):
        return -self.controller.get_axis(RIGHT_Y)
