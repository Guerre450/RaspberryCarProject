import board
import busio
from time import sleep
import adafruit_bus_device.i2c_device as i2c_device
from adafruit_ht16k33 import matrix
import threading

class Matrix(threading.Thread):


    def run(self):
        self.kill = False
        i2cBus = busio.I2C(board.SCL, board.SDA)
        module = i2c_device.I2CDevice(i2cBus, 0x70)
        i2c = busio.I2C(board.SCL, board.SDA)
        mat = matrix.Matrix8x8(i2c)
        self.isNeeded = False

        while not self.kill:
            if self.isNeeded:
                #pour fix un bug avec adafruit_ht16k33
                mat.fill(1)
                sleep(0.10)
                mat.fill(0)
                octetX = 128
                octetY = 1
                for i in range(0,16,2):
                    module.write(bytes([i]))
                    module.write(bytes([i,octetX + octetY])) 
                    octetX = octetX >> 1
                    octetY = octetY << 1
                    sleep(0.05)
                for i in range(16,-2,-2):
                    module.write(bytes([i]))
                    module.write(bytes([i,0])) 
                    octetX = octetX >> 1
                    octetY = octetY << 1
                    sleep(0.05)
                self.isNeeded = False