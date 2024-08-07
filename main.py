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
    key = keypad.GetKey()
    if key:
      lock_system.prompt_for_code()

    lock_system.check_autolock()
    sleep(0.5)