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
 
while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        elif event.type == pygame.JOYBUTTONDOWN:

            if event.button == 0:  # A button

                print("A button pressed")
                joystick.rumble(low_frequency=0.3,high_frequency=5,duration=300)

            elif event.button == 1:  # B button

                print("B button pressed")

            elif event.button == 2:  # X button

                print("X button pressed")

            elif event.button == 3:  # Y button

                print("Y button pressed")

            elif event.button == 4:  # Left bumper

                print("eft bumper pressed")

            elif event.button == 5:  # Right bumper

                print("Right bumper pressed")
            elif event.button == 11:
                print('not caca')

        elif event.type == pygame.JOYBUTTONUP:

            if event.button == 0:  # A button

                print("A button released")

            elif event.button == 1:  # B button

                print("B button released")

            elif event.button == 2:  # X button

                print("X button released")

            elif event.button == 3:  # Y button

                print("Y button released")

            elif event.button == 4:  # Left bumper

                print("Left bumper released")

            elif event.button == 5:  # Right bumper

                print("Right bumper released")
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 4:  # Left trigger axis
                print(f"Left trigger axis: {event.value}")
            elif event.axis == 5:  # Right trigger axis
                print(f"Right trigger axis: {event.value}")
        # Limit to 20 frames per second

    clock.tick(20)
 
# Quit Pygame

pygame.quit()
 