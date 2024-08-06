from machine import Pin

ROWS = 4
COLS = 4
KEYS = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

ROW_PINS = [6, 7, 8, 9]
COL_PINS = [10, 11, 12, 13]

row_pins = [Pin(ROW_PINS[0], Pin.OUT), Pin(ROW_PINS[1], Pin.OUT), Pin(ROW_PINS[2], Pin.OUT), Pin(ROW_PINS[3], Pin.OUT)]
col_pins = [Pin(COL_PINS[0], Pin.IN, Pin.PULL_DOWN), Pin(COL_PINS[1], Pin.IN, Pin.PULL_DOWN), Pin(COL_PINS[3], Pin.IN, Pin.PULL_DOWN), Pin(COL_PINS[3], Pin.IN, Pin.PULL_DOWN)]

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