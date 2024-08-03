#include <Arduino.h>
#include <LiquidCrystal.h>

#include "lcd.h"
#include "Lock.h"
#include "keypad_x.h"

LiquidCrystal lcd(LCD_PIN1, LCD_PIN2, LCD_PIN3, LCD_PIN4, LCD_PIN5, LCD_PIN6);

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
  
  Lock session();
  session->startSession();

  String result = "";
  while (result.length() < 4) {
    char key = keypad.getKey();
    if (lcdValidateKey(key)) {
      lcd.print('*');
      result += key;
    }
  }

  bool result = session->enterCode(result);
  if (!result) {
    lcdFailScreen();
    delay(3000);
    lcdLockScreen();
  }
}