import board
import busio
from time import sleep
from adafruit_ht16k33 import matrix

i2c = busio.I2C(board.SCL, board.SDA)
mat = matrix.Matrix8x8(i2c)

mat[2,2] = 1
sleep(1)
mat.fill(0) # 