#ifndef LOCK_H
#define LOCK_H

class Lock {
public:
  Lock();
  bool startSession();
  bool enterCode(String code);

private:
  static const int LOCK_CODE = 1234;
  static const int MAX_TRIES = 3;
  int tries;
  bool sessionActive;
};

#endif
