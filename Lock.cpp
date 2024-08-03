#include "Lock.h"

Lock::Lock() : tries(0), sessionActive(false) {}

bool Lock::startSession() {
  if (sessionActive) {
    return false;
  }

  tries = 0;
  sessionActive = true;
  return true;
}

bool Lock::enterCode(int code) {
  if (!sessionActive) {
    return false;
  }

  if (code == LOCK_CODE) {
    sessionActive = false;
    return true;
  }

  tries++;
  if (tries >= MAX_TRIES) {
    sessionActive = false;
    return false;
  }

  return false;
}
