import pigpio

def forward(pi):
    gpioList1 = [20,19]
    gpioList0 = [21,26]
    for i in gpioList1:
        pi.write(i,1)

    for i in gpioList0:
        pi.write(i,0)


def reverse(pi):
    num = 1
    gpioList = [21,20,26,19]
    for i in gpioList:
        pi.set_mode(i,pigpio.OUTPUT)
        pi.write(i, num % 2)
        num += 1


def left(pi):
    num = 1
    gpioList = [26,19]
    for i in gpioList:
        pi.set_mode(i,pigpio.OUTPUT)
        pi.write(i, num % 2)
        print(num % 2)
        num += 1
def right(pi):
    num = 1
    gpioList = [20,21]
    for i in gpioList:
        pi.set_mode(i,pigpio.OUTPUT)
        pi.write(i, num % 2)
        print(num % 2)
        num += 1

def stop(pi):
    gpioList = [20,21,26,19]
    for i in gpioList:
        pi.write(i, 0)
