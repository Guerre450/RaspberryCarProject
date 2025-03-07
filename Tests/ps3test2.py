
import pygame
 
# Initialize Pygame

pygame.init()
 
# Initialize the joystick module

pygame.joystick.init()
 
# Get count of joysticks

joystick_count = pygame.joystick.get_count()
 
# Create a joystick object

joystick = pygame.joystick.Joystick(0)

joystick.init()
 
# Main program loop

done = False

clock = pygame.time.Clock()
hats = joystick.get_numhats()
while not done:
    for i in range(hats):
            hat = joystick.get_hat(i)

            if hat[1] == 1:
                speedfactor += 0.05
            elif hat[1] == -1:
                speedfactor -= 0.05
            elif hat[0] == -1:
                speedlimit -= 5
            elif hat[0] == 1:
                speedlimit += 5

            if speedlimit >= 100:
                speedlimit = 100
            if speedlimit <= 0:
                speedlimit = 0
            if speedfactor >= 5:
                speedfactor = 5
            if speedfactor <= 0:
                speedfactor = 0

pygame.close()