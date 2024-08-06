#include "srvo.h"

#include <Servo.h>

Servo servo;

void setupServo() {
  servo.attach(SERVO_PIN);
}

void lockServo() {
  servo.write(SERVO_LOCK);
}

void unlockServo() {
  servo.write(SERVO_UNLOCK);
}