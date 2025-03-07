import pigpio
import threading
import time
class FrontLed(threading.Thread):

    def run(self):
        self.kill = False

        pi = pigpio.pi()
        LED = 27
        pi.set_mode(LED,pigpio.OUTPUT)


        self.isPressed = False

        isSet = False
        canSet = True
        while not self.kill:
            if self.isPressed and canSet:
                isSet = not isSet
                canSet = False
            elif not self.isPressed:
                canSet = True
            pi.write(LED,1) if isSet else pi.write(LED,0)
        pi.write(LED,0)
