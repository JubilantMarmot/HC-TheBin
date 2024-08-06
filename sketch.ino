#include <Arduino.h>
#include <Servo.h>

#include "lcd.h"
#include "srvo.h"

void setup() {
  setupServo();
  setupLcd();
}

void loop() {
  lcdWelcome();
  delay(5000);
  lcdLockScreen();
}