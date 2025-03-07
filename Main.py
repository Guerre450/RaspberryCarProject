import pigpio
import time
from enum import Enum
import pygame
from WheelHandler import WheelHandler
from Led import FrontLed 
from DriverHandler import DriverHandler, DriveAction
from Matrix import Matrix
from LCD import TextScreen
import threading
from Button import Button 
from SuperSonique import DetectorHandler
gpioList = [21,20,19,26]
pi = pigpio.pi()
matrix = Matrix()
textScreen = TextScreen()
wheelHandler = WheelHandler(pi=pi)
frontLed = FrontLed()
detectorHandler = DetectorHandler()
driverHandler = DriverHandler(pi=pi,matrix=matrix, textScreen=textScreen, detector=detectorHandler)

threads = [matrix,textScreen,wheelHandler,frontLed,detectorHandler, driverHandler]

for i in threads:
    i.start()
print("threads started")

# Initialize Pygame

pygame.init()
 
# Initialize the joystick module

pygame.joystick.init()
 
# Get count of joysticks

joystick_count = pygame.joystick.get_count()
 
# Create a joystick object
if (joystick_count < 1):
    print("Joystick count lower than 1, controller not connected")
if not (joystick_count < 1):
    joystick = pygame.joystick.Joystick(0)

    joystick.init()


clock = pygame.time.Clock()



class BUTTONS(Enum):
    X = 0
    O = 1
    TRIANGLE = 2
    SQUARE = 3
    L1 = 4
    R1 = 5
stateList = {
    "X" : False,
    "O" : False,
    "TRIANGLE" : False,
    "SQUARE" : False,
    "L1" : False,
    "R1" : False,
}

button = Button(17,pi)

lastXaxis = 0.0
lastBumper = 0.0

done = False
while not done and not (joystick_count < 1):
    button.detectPress()
    if button.getState():
        print("EMERGENCY SHUTDOWN ACTIVATED")
        done = True
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        elif event.type == pygame.JOYBUTTONDOWN:

            if event.button == BUTTONS.X.value:  # A button
                stateList["X"] = True

            elif event.button == BUTTONS.O.value:  # B button
                stateList["O"] = True
            elif event.button == BUTTONS.TRIANGLE.value:
                done = True
            elif event.button == BUTTONS.SQUARE.value:
                stateList["SQUARE"] = True
            elif event.button == BUTTONS.L1.value:  # Left bumper

                stateList["L1"] = True

            elif event.button == BUTTONS.R1.value:  # Right bumper
                stateList["R1"] = True

        elif event.type == pygame.JOYBUTTONUP:

            if event.button == BUTTONS.X.value:  # A button

                stateList["X"] = False

            elif event.button == BUTTONS.O.value:  # B button

                stateList["O"] = False
            elif event.button == BUTTONS.SQUARE.value:
                stateList["SQUARE"] = False

            elif event.button == BUTTONS.L1.value:  # Left bumper

                stateList["L1"] = False

            elif event.button == BUTTONS.R1.value:  # Right bumper

                stateList["R1"] = False
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:  # Left stick X-axis
                lastXaxis = event.value
            elif event.axis == 5:  # Right trigger axis
                lastBumper = event.value
    if driverHandler.driveAction != DriveAction.WARNING:
        wheelHandler.xAxis = lastXaxis
        wheelHandler.bumper = lastBumper
        if stateList["X"] and stateList["O"] or not stateList["X"] and  not stateList["O"] or wheelHandler.bumper <= 0:
            driverHandler.driveAction = DriveAction.STOPPED
        elif stateList["X"]:
            driverHandler.driveAction = DriveAction.FORWARD
        elif stateList["O"]:
            driverHandler.driveAction = DriveAction.REVERSE
    else:
        wheelHandler.xAxis = 0.0
        wheelHandler.bumper = 0.7
    if driverHandler.rumble:
        joystick.rumble(low_frequency=0.3,high_frequency=5,duration=300)
        driverHandler.rumble = False
    

    frontLed.isPressed = stateList["SQUARE"]

    # if stateList["L1"] and stateList["R1"] or not stateList["L1"] and  not stateList["R1"]:
    #     turnHandler.currentAction = TurnAction.NONE
    # elif stateList["L1"]:
    #     turnHandler.currentAction = TurnAction.LEFT
    # elif stateList["R1"]:
    #     turnHandler.currentAction = TurnAction.RIGHT

    # Limit to 20 frames per second
    clock.tick(60)

pygame.quit()

#waiting for all threads to be killed
threadsAmount = len(threads)
allthreadsEndedNum = threading.active_count() - threadsAmount
for i in threads:
    i.kill = True
while threading.active_count() > allthreadsEndedNum:
    print("waiting for {0} threads".format(str(threading.active_count() - allthreadsEndedNum)))
    time.sleep(1)

print("Program end")