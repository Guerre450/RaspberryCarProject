import threading
import time
from enum import Enum
from TurnRate import turnRate
from ServoMoteur import servo


class TurnAction(Enum):
    LEFT = 1
    RIGHT = 2
    NONE = 3
class WheelHandler(threading.Thread):

    def __init__(self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None, pi = None):
        self.pi = pi
        super().__init__(group, target, name, args, kwargs, daemon=daemon)

    def run(self):
        self.bumper = 0.0
        self.xAxis = 0.0
        data = 50
        turnRate(self.pi,data)
        servo(self.pi,data)

        self.kill = False
        self.currentAction = TurnAction.NONE
        while not self.kill:
            data = int((self.xAxis + 1) / 2 * 100) % 101
            bumperPercent = self.bumper if self.bumper >= 0 else 0
            #print(bumperPercent)
            turnRate(self.pi,data, bumperPercent)
            servo(self.pi,data)
            # if self.currentAction == TurnAction.LEFT:
            #     data = data - 5 if data > 0 else data
            #     data = abs(data)
            #     data = data % 100
            #     turnRate(self.pi,data)
            #     servo(self.pi,data)
            # elif self.currentAction == TurnAction.RIGHT:
            #     data = data + 5 if data < 100 else data
            #     data = data % 101
            #     print(data)
            #     turnRate(self.pi,data)
            #     servo(self.pi,data)
            # else:
            #     pass
            time.sleep(0.05)

