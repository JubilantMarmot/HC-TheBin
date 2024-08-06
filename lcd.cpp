#include <Arduino.h>
#include <LiquidCrystal.h>

#include "lcd.h"
#include "Lock.h"
#include "keypad.h"

LiquidCrystal lcd(LCD_PIN1, LCD_PIN2, LCD_PIN3, LCD_PIN4, LCD_PIN5, LCD_PIN6);

/////\\\\\
#include <Keypad.h>

#include "keypad.h"

const short KEYPAD_ROWS = 4;
const short KEYPAD_COLS = 4;

byte KEYPAD_ROW_PINS[KEYPAD_ROWS] = {16, 17, 18, 19};
byte KEYPAD_COL_PINS[KEYPAD_COLS] = {20, 21, 22, 26};

char KEYPAD_KEYS[KEYPAD_ROWS][KEYPAD_COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

Keypad keypad = Keypad(makeKeymap(KEYPAD_KEYS), KEYPAD_ROW_PINS, KEYPAD_COL_PINS, KEYPAD_ROWS, KEYPAD_COLS);
/////\\\\\

bool lcdValidateKey(char key) {
  if (key >= '0' && key <= '9') {
    return true;
  }

  return false;
}

void setupLcd() {
  lcd.begin(16, 2);
}

void lcdWelcome() {
  lcd.setCursor(4, 0);
  lcd.print("Welcome!");
  delay(1000);
}

void lcdLockScreen() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Locked; enter code");

  lcdPromptCode();
}

void lcdFailScreen() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Incorrect code!");
}

void lcdPromptCode() {
  lcd.setCursor(5, 1);
  lcd.print("[____]");
  
  Lock* session;
  session->startSession();

  String result = "";
  while (result.length() < 4) {
    char key = keypad.getKey();
    if (lcdValidateKey(key)) {
      lcd.print('*');
      result += key;
    }
  }

  bool codeResult = session->enterCode(result);
  if (!codeResult) {
    lcdFailScreen();
    delay(3000);
    lcdLockScreen();
  }
}