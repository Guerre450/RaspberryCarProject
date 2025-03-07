import pigpio
class Button:
    def __init__(self, pin,pi) -> None:
        self.pi = pi
        self.pin = pin
        self.isPressed = False
        self.count = 0
        pi.set_mode(pin,pigpio.INPUT)
        pi.set_pull_up_down(pin,pigpio.PUD_UP)
        
    def detectPress(self):
        if self.pi.read(self.pin) == 0:
            if not self.isPressed:
                self.count += 1
                if self.count >= 4:
                    self.isPressed = True
        else:
            self.count = 0
            self.isPressed = False
    def getState(self):
        return self.isPressed