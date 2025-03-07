from CarCommands import forward,reverse,left,right,stop
from SuperSonique import distance
import time
import pigpio

pi = pigpio.pi()
time.sleep(5)
canRun = True
turn = 0
RIGHT, LEFT = 12,6
pi.set_mode(RIGHT, pigpio.OUTPUT)
pi.set_mode(LEFT, pigpio.OUTPUT)
pi.set_PWM_dutycycle(RIGHT,255)
pi.set_PWM_dutycycle(LEFT,255)
try:
    forward(pi)
    while canRun:
        pass
    stop(pi)
except KeyboardInterrupt:
    stop(pi)