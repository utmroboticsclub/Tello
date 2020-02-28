import tello
import time


class TelloPID:
    # A PID object for use with
    def __init__(self, kP=0, kI=0, kD=0):
        self.kP = kP
        self.kI = kI 
        self.kD = kD
        self.p = 0
        self.i = 0
        self.d = 0
        self.current_value = 0
        self.current_time = time.time()
        self.last_value = 0
        self.last_time = time.time()

    def start(self, targetVal):
        self.targetVal = targetVal

    def update(self, value):
        self.last_value = self.current_value
        self.current_value = value
        self.last_time = self.current_time
        self.current_time = time.time()
        self.p = self.current_value - self.last_value
        self.update_time_delta = self.current_time - self.last_time
        if self.kI != 0:
            self.i += self.p
        if self.update_time_delta > 0:
            self.d = self.kD*(self.current_value - self.last_value)/(self.update_time_delta)
        self.output = self.kP*self.p + self.kI*self.i - self.kD*self.d
        return self.output

    def getOutput(self):
        return self.output