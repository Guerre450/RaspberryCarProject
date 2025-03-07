import pigpio



def servo(pi,percent):
    servo = 22
    FREQ = 50

    pi.set_mode(servo,pigpio.OUTPUT)
    pi.set_PWM_frequency(servo,FREQ)
    pi.set_PWM_range(servo,100)

    #MAXRANGE = 12.5
    MINRANGE= 3.0
    RANGE= 9.5
    amount = (RANGE - (percent/100 * RANGE)) + MINRANGE
    pi.set_PWM_dutycycle(servo,amount)