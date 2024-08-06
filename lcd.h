#ifndef LCD_H
#define LCD_H

#include <Arduino.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

#include "lcd.h"
#include "Lock.h"

#define LCD_PIN1 12
#define LCD_PIN2 11
#define LCD_PIN3 10
#define LCD_PIN4 9
#define LCD_PIN5 8
#define LCD_PIN6 7

class KeypadLCD {
public:
    // Constructor that takes a Keypad object by reference
    KeypadLCD(Keypad& keypad);

    // Public methods
    void setupLcd();
    void lcdWelcome();
    void lcdLockScreen();
    void lcdFailScreen();

private:
    Keypad& keypad; // Reference to the Keypad object
    LiquidCrystal lcd; // LiquidCrystal object for controlling the LCD

    // Private methods
    bool lcdValidateKey(char key);
    void lcdPromptCode();
};

#endif