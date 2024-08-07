import servo
import buzzer
import screen
import keypad
import lock

from math import floor
from utime import sleep
import time

lock_system = lock.LockSystem()

def Welcome():
  screen.Write("Lock initialized")
  sleep(0.5)
  lock_system.lock()

Welcome()

lastKey = time.time()
while True:
    if lock_system.locking:
      sleep(3)

    lock_system.check_autolock()
    key = keypad.GetKey()
    if key:
      if lock_system.locked:
        lock_system.prompt_for_code(key)
      else:
        if key == "#":
          lock_system.lock()

    sleep(0.5)