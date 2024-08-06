#ifndef LOCK_H
#define LOCK_H

#include <Arduino.h>

const String LOCK_CODE = "1234";

class Lock {
public:
  Lock();
  bool startSession();
  bool enterCode(String code);

private:
  static const int MAX_TRIES = 3;
  int tries;
  bool sessionActive;
};

#endif