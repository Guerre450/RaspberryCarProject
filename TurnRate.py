
import pigpio
def turnRate(pi ,percent, speedPercentage = 1):
    global pigpio
    LEFT,RIGHT = 12,6
    MAXSPEED = 255
    currentSpeed = int(MAXSPEED * speedPercentage)
    pi.set_mode(RIGHT, pigpio.OUTPUT)
    pi.set_mode(LEFT, pigpio.OUTPUT)
    if percent < 45:
        amount = percent / 50 * 255
        pi.set_PWM_dutycycle(RIGHT,amount)
        pi.set_PWM_dutycycle(LEFT,currentSpeed)
    elif percent > 55:
        amount = (50 - (percent - 50)) / 50 * 255
        pi.set_PWM_dutycycle(LEFT,amount)
        pi.set_PWM_dutycycle(RIGHT,currentSpeed)
    else:
        pi.set_PWM_dutycycle(RIGHT,currentSpeed)
        pi.set_PWM_dutycycle(LEFT,currentSpeed)
