from machine import Pin
import pins

ROWS = 4
COLS = 4
KEYS = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

row_pins = [
    Pin(pins.KEYPAD_ROWS[0], Pin.OUT),
    Pin(pins.KEYPAD_ROWS[1], Pin.OUT),
    Pin(pins.KEYPAD_ROWS[2], Pin.OUT),
    Pin(pins.KEYPAD_ROWS[3], Pin.OUT)
]

col_pins = [
    Pin(pins.KEYPAD_COLS[0],Pin.IN, Pin.PULL_DOWN),
    Pin(pins.KEYPAD_COLS[1], Pin.IN, Pin.PULL_DOWN),
    Pin(pins.KEYPAD_COLS[2], Pin.IN, Pin.PULL_DOWN),
    Pin(pins.KEYPAD_COLS[3], Pin.IN, Pin.PULL_DOWN)
]

def GetKey():
    for r in range(ROWS):
        row_pins[r].value(1)
        for c in range(COLS):
            if col_pins[c].value():
                while col_pins[c].value():
                    pass
                row_pins[r].value(0)
                return KEYS[r][c]
        row_pins[r].value(0)
    return None