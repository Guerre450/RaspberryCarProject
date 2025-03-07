import threading
import time
from CarCommands import forward, reverse, left, right, stop
from Potensiometre import potensioMeterAmount
from enum import Enum

class DriveAction(Enum):
    FORWARD = 1
    REVERSE = 2
    STOPPED = 3
    WARNING = 4
class DriverHandler(threading.Thread):

    def __init__(self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None, pi = None, matrix = None, textScreen = None, detector):
        self.pi = pi
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.matrix = matrix
        self.textScreen = textScreen
        self.detector = detector
    def run(self):
        #Matrix Animation
        
        self.driveAction = DriveAction.STOPPED
        self.rumble = False
        LOWESTSENTIVITY = 5
        SENSITIVITYRANGE = 40
        self.kill = False
        while not self.kill:
            potenAmount = potensioMeterAmount()
            stopDistance = ((potenAmount/ 100) * SENSITIVITYRANGE) + LOWESTSENTIVITY
            wallDistance = self.detector.value
            self.textScreen.msg2 = "Distance :" + str(round(stopDistance,2))
            if wallDistance < (stopDistance) :
                self.driveAction = DriveAction.WARNING
                self.matrix.isNeeded = True
                self.rumble = True
                stop(self.pi)
                reverse(self.pi)
                time.sleep(1)
                stop(self.pi)
                time.sleep(0.5)
                self.driveAction = DriveAction.STOPPED
                
            else:
                #print(self.driveAction)
                match self.driveAction:
                    case DriveAction.FORWARD:
                        forward(self.pi)
                    case DriveAction.REVERSE:
                        reverse(self.pi)
                    case DriveAction.STOPPED:
                        stop(self.pi)
