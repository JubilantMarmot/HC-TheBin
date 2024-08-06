from ssd1306 import SSD1306_I2C
from machine import Pin, PWM, I2C

SCREEN_SDA = 0
SCREEN_SCL = 1
SCREEN_FREQ = 400000

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, sda=Pin(SCREEN_SDA), scl=Pin(SCREEN_SCL), freq=SCREEN_FREQ)
oled = SSD1306_I2C(128, 64, i2c)

def Write(text, clear = True, x = 0, y = 0):
    if clear:
        oled.fill(0)
    
    oled.text(text, x, y)
    oled.show()
