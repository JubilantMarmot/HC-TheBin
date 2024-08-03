#ifndef LCD_H
#define LCD_H

#define LCD_PIN1 12
#define LCD_PIN2 11
#define LCD_PIN3 10
#define LCD_PIN4 9
#define LCD_PIN5 8
#define LCD_PIN6 7

void setupLcd();

void lcdWelcome();
void lcdPromptCode();
void lcdLockScreen();
bool lcdValidateKey(char key);

#endif
