#include <Arduino.h>
#include <Servo.h>
#include <Keypad.h>

#include "lcd.h"
#include "srvo.h"
#include "lcd.h"

const byte KEYPAD_ROWS = 4;
const byte KEYPAD_COLS = 4;
byte rowPins[KEYPAD_ROWS] = {5, 4, 3, 2};
byte colPins[KEYPAD_COLS] = {A3, A2, A1, A0};
char keys[KEYPAD_ROWS][KEYPAD_COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, KEYPAD_ROWS, KEYPAD_COLS);

KeypadLCD keypadLCD(keypad);

void setup() {
  setupServo();
  keypadLCD.setupLcd();
}

void loop() {
  keypadLCD.lcdWelcome();
  delay(5000);
  keypadLCD.lcdLockScreen();
}