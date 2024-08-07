from ssd1306 import SSD1306_I2C
from machine import Pin, PWM, I2C
import pins

SCREEN_FREQ = 400000

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, sda=Pin(pins.SCREEN_SDA), scl=Pin(pins.SCREEN_SCL), freq=SCREEN_FREQ)
oled = SSD1306_I2C(128, 64, i2c)

def Write(text, clear = True, x = None, y = None, x2 = 0, y2 = 0):
    if clear:
        oled.fill(0)
    
    text_width = len(text) * 8
    text_height = 8

    if x is None:
        x = (WIDTH - text_width) // 2
    
    if y is None:
        y = (HEIGHT - text_height) // 2
    
    x = x + x2
    y = y + y2

    oled.text(text, x, y)
    oled.show()
