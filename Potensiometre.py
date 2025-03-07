import busio
import board
from adafruit_ads1x15.ads1115 import ADS1115, P0
from adafruit_ads1x15.analog_in import AnalogIn

def potensioMeterAmount() -> int:
        MAXVOLTAGE = 5
        i2c = busio.I2C(board.SCL, board.SDA,)
        ads = ADS1115(i2c, 2/3)
        data = AnalogIn(ads, P0)
        return round(abs(data.voltage) / MAXVOLTAGE * 100)
