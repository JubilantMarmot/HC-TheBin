#include <Keypad.h>

#include "keypad_x.h"


const short KEYPAD_ROWS = 4;
const short KEYPAD_COLS = 4;

byte KEYPAD_ROW_PINS[KEYPAD_ROWS] = {5, 4, 3, 2};
byte KEYPAD_COL_PINS[KEYPAD_COLS] = {5, 4, 3, 2};

char KEYPAD_KEYS[KEYPAD_ROWS][KEYPAD_COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

Keypad keypad = Keypad(makeKeymap(KEYPAD_KEYS), KEYPAD_ROW_PINS, KEYPAD_COL_PINS, KEYPAD_ROWS, KEYPAD_COLS);

